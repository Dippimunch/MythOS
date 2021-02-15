import dictionary as dic
import random
from entities import *
import XSAMPA as xsam
import re



strings = ['in a time before time', 'long ago', 'when all was naught but light']

def fillLocation(location):
    for p in range(location.population):
        person = Person(p, 20)
        location.list.append(person)

def makePerson():
    pass
        
def randomLanguage():
    con_num = random.randrange(20, 30)
    vowel_num = random.randrange(2, 6)
    
    c_chart = list(xsam.consonants.keys())
    v_chart = list(xsam.vowels.keys())

    words = {}
    base = random.choice([5, 6, 8, 10, 12, 15, 16, 18, 20, 24])
    numbers = {}
    
    vowels = []
    v_choice = None

    cons = []
    c_choice = None

    syllables = []

    name = 'Name'

    # add vowels
    for v in range(vowel_num):
        v_choice = random.choice(v_chart)
        vowels.append(v_choice)
        v_chart.remove(v_choice)

    # add consonants
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

    for i in range(2,5):
        power_number = ''
        length = random.randrange(1, 3)
        for s in range(length):
            number += syllable(vowels, cons)
        words[str(base**i)] = power_number
                
        # CONCEPT OF ZERO?
        # '10s' '100s' '1000s' place 'dozen' 'gross'

    return Language(name, cons, vowels, base, words)

# syllable[onset][rhyme[nucleus][coda]]
# TODO: rules
# https://wals.info/chapter/12
def syllable(vowels, cons):
    # CV constant?
    # some (C)V where () is optional
    # English complex syllable structure (C)(C)(C)V(C)(C)(C)(C)
    onset = random.choice(cons)
    nucleus = random.choice(vowels)
    coda = random.choice(cons)
    rhyme = '%s%s' % (nucleus, coda)
    unit = '%s%s' % (onset, rhyme)

    return unit

def feature_choice(feature):
    #feature
    pass

def latinize(text):
    pass

#print(language.consonants)

# generalize
#def town():
#   print(dic.pick('pronoun' or 'verb'))

    
