import dictionary as dic
import random
from entities import *
import XSAMPA as xsam
import re


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
    if random.random() < .519:
        sex = 'male'
    else:
        sex = 'female'
    person = Person(name, age, sex, lang, kin)
    return person
        
def randomLanguage():
    con_num = random.randrange(12, 30)
    vowel_num = random.randrange(2, 6)
    
    c_chart = list(xsam.consonants.keys())
    v_chart = list(xsam.vowels.keys())

    words = {}
    # number base- should change to more restricted choices
    base = random.randrange(2, 24)
    numbers = {}
    
    vowels = []
    v_choice = None

    cons = []
    c_choice = None

    syllables = []

    name = 'Name'

    for v in range(vowel_num):
        v_choice = random.choice(v_chart)
        vowels.append(v_choice)
        v_chart.remove(v_choice)

    for c in range(con_num):
        c_choice = random.choice(c_chart)
        cons.append(c_choice)
        c_chart.remove(c_choice)

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

    return Language(name, cons, vowels, base, words)

# syllable[onset][rhyme[nucleus][coda]]
# TODO: rules
# https://wals.info/chapter/12
def syllable(vowels, cons):
    pre_restrict = None
    post_restrict = None
    # CV constant?
    # some (C)V where () is optional
    # English complex syllable structure (C)(C)(C)V(C)(C)(C)(C)
    syll_struct = None
    comp = random.randint(1, 100)

    """if comp <= 13:
        syll_struct = 'Simple'
    elif comp > 13 and comp <= 43:
        syll_struct = 'Complex'
    else:
        syll_struct = 'Moderate'

    if syll_struct == 'Simple':"""            
    onset = random.choice(cons)
    nucleus = random.choice(vowels)
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

    
