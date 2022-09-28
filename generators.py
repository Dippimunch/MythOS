import dictionary as dic
import random
from entities import *
import XSAMPA as xsam
import re
import numpy as np


# https://pvigier.github.io/2018/06/13/perlin-noise-numpy.html
# shape of the generated array (tuple of 2 ints)
def generate_perlin_noise_2d(shape, res):
    def f(t):
        return 6*t**5 - 15*t**4 + 10*t**3

    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0],0:res[1]:delta[1]].transpose(1, 2, 0) % 1
    # Gradients
    angles = 2*np.pi*np.random.rand(res[0]+1, res[1]+1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    g00 = gradients[0:-1,0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g10 = gradients[1:,0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g01 = gradients[0:-1,1:].repeat(d[0], 0).repeat(d[1], 1)
    g11 = gradients[1:,1:].repeat(d[0], 0).repeat(d[1], 1)
    # Ramps
    n00 = np.sum(grid * g00, 2)
    n10 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:,:,0], grid[:,:,1]-1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:,:,0]-1, grid[:,:,1]-1)) * g11, 2)
    # Interpolation
    t = f(grid)
    n0 = n00*(1-t[:,:,0]) + t[:,:,0]*n10
    n1 = n01*(1-t[:,:,0]) + t[:,:,0]*n11
    return np.sqrt(2)*((1-t[:,:,1])*n0 + t[:,:,1]*n1)

def generate_fractal_noise_2d(shape, res, octaves=1, persistence=0.5):
    noise = np.zeros(shape)
    frequency = 1
    amplitude = 1
    for _ in range(octaves):
        noise += amplitude * generate_perlin_noise_2d(shape, (frequency*res[0], frequency*res[1]))
        frequency *= 2
        amplitude *= persistence
    return noise
# generate_perlin_noise_2d((5,5), (10,10)) ValueError: operands could not be broadcast together with shapes (5,5,2) (0,0,2)

def randomLocation(size):
    name = None
    features = None
    for s in range(size):
        pass
    #location = Location(

def fillLocation(location):
    for p in range(location.population):
        person = randomPerson()
        location.list.append(person)

def randomPerson():
    name = '%s-%s' % (random.choice(get_key('adjective', dic.swadesh)), random.choice(get_key('noun', dic.swadesh)))
    age = random.randrange(70)
    sex = 'male'
    lang = None
    kin = None
    location = None
    if random.random() < .519:
        sex = 'male'
    else:
        sex = 'female'
    person = Person(name, age, sex, lang, kin, location)
    return person
        
def randomLanguage():
    con_num = random.randrange(12, 30)
    vowel_num = random.randrange(2, 6)
    
    c_chart = list(xsam.consonants.values())
    v_chart = list(xsam.vowels.values())

    words = {}
    # number base- should change to more restricted choices
    base = random.randrange(2, 24)
    numbers = {}
    
    vowels = []
    v_choice = None

    cons = []
    c_choice = None

    #syll_cmplx = random.randrange(2)
    syll_struct = []
    syllables = []

    name = 'Name'

    

    # phonemic inventory creation
    # from allowed syll_struct
    # 'CCV' / for i in range: if i = C choose from allowed cons elif V choose from allowed vowels else choose 'uni'[i]
    for v in range(vowel_num):
        for i in range(len(v_chart)):
            v_choice = random.choice(v_chart[i]['uni'])
            vowels.append(v_choice)
        #v_chart.remove(v_choice)

    for c in range(con_num):
        for i in range(len(c_chart)):
            c_choice = random.choice(c_chart[i]['uni'])
            cons.append(c_choice)
        #c_chart.remove(c_choice)
            

    # add words to dictionary
    for key in dic.swadesh.keys():
        word = ''
        length = random.randrange(1, 3)
        for s in range(length):
            word += syllable(vowels, cons)
        words[key] = word

    for n in range(base):
        number = ''
        length = random.randrange(1, 3)
        for s in range(length):
            number += syllable(vowels, cons)
        words[str(n)] = number
        # CONCEPT OF ZERO?

    return Language(name, cons, vowels, syll_struct, base, words)

# syllable[onset][rhyme[nucleus][coda]]
# TODO: rules
# https://wals.info/chapter/12
def syllable(vowels, cons):
    pre_restrict = None
    post_restrict = None
    # CV constant?
    # some (C)V where () is optional
    # English complex syllable structure (C)(C)(C)V(C)(C)(C)(C)
    struct_type = None
    r = random.randrange(0, 458)
    if r <= 60:
        struct_type = 'simple'
    elif r > 60 and r <= 273:
        struct_type = 'moderately complex'
    else:
        struct_type = 'complex'
        
    # a consonant or consonant cluster, obligatory in some languages, optional or even restricted in others
    onset = random.choice(cons)
    
    # Rime - contrasts with onset, splits into nucleus and coda
    
    # a vowel or syllabic consonant, obligatory in most languages
    nucleus = random.choice(vowels)
    
    # consonant, optional in some languages, highly restricted or prohibited in others
    coda = random.choice(cons)
    
    rhyme = '%s%s' % (nucleus, coda)
    unit = '%s%s' % (onset, rhyme)

    return unit

def story(text, location=None):
    strings = ['in a time before time', 'long ago', 'when all was naught but light']

    subject = random.choice(get_key('noun', dic.swadesh))
    subject_2 = random.choice(get_key('noun', dic.swadesh))
    subject_3 = random.choice(get_key('noun', dic.swadesh))
    action = random.choice(get_key('verb', dic.swadesh))
    action_2 = random.choice(get_key('verb', dic.swadesh))
    # fstring variables
    text_out = f"the {subject} {action}s the {subject_2} in order to {action_2} a {subject_3}"
    print(text_out)

def feature_choice(feature):
    #feature
    pass

# function to return key for any value
def get_key(val, dic):
    keys = []
    for i in dic.items():
        if i[1] == val:
            keys.append(i[0])
    return keys
        
def latinize(text):
    pass


#print(language.consonants)

# generalize
#def town():
#   print(dic.pick('pronoun' or 'verb'))

    
