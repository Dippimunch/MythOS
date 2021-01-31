# GOal to get rid of this, everything is/should be elsewhere


import random
import dictionary as dic

# Two systems to eventually create
# A Representational (Prescriptive?) and a Descriptive
# (Does a language exist outside its usuage?)
class Language:
    culture = None
    
    def __init__(self):
        phoneInv = []
        syllable = []
        word = {}

        #filling swadesh
        for key in dic.swadesh:
            #word[key] = 
            #iterate over dictionary
            pass
        

class Phoneme:
    consonant = 'bcdfghjklmnpqrstvwxz'
    vowel = 'aeiou'
        
    
    
consonant = 'bcdfghjklmnpqrstvwxz'
vowel = 'aeiou'
syllable = []
word = []
wordCount = 10

dictionary = ['cat', 'dog', 'fox', 'water', 'air']
elements = {'fire' : [], 'water' : [], 'air' : [], 'earth' : ['static']}
# poly = True

# pre/suffix
# conjugation


# consonantNumber = random.randint(0, 2)
# vowelNumber = random.randint(0, 2)


#Syllable Construction
# CV/CVV/CVC/etc
for x in range(0, 10):
    for y in range(0, 2):
        syllable.append(random.choice(consonant) + random.choice(vowel))

# Wordlist Construction
for i in range(0, len(dictionary)):
    word.append(syllable[random.randint(0, len(syllable) - 1)])
    for j in range(0, random.randint(0, 3)):
        word[i] = word[i] + syllable[random.randint(0, len(syllable) - 1)]
# subjective, objective, possessive
# nominative, accusative, gentitive, dative
#case():

#noun = {'Pronoun' : ['firstSing', 'secSing', 'thrdSing']}
noun = ['person', 'animal', 'element', 'object', 'idea', "two/pair",
        "tongue", "name", "eye", "heart", "tooth", "finger-nail",
        "louse", "teardrop", "water"]
#verb = {'Active' : ['look', 'take']}
verb = ['looked at', 'heard', 'take', 'gave to', 'went to', 'made', 'see']
adjective = ['red', 'blue', 'yellow', 'big', 'small', 'good', 'bad',
             'dead', 'old', 'new']
count = ['one', 'two/pair']

class Animal:
    def __init__(self, name, size, **kwargs):
        self.name = name
        self.size = size
        self.attributes = {kwargs}
# iterate
#

class Word:
    def __init__(self):
        #attributes
        pass

def rude_phrase():
    print("The %s %s %s the %s %s" % (random.choice(adjective), random.choice(noun),
                                      random.choice(verb), random.choice(adjective),
                                      random.choice(noun)))
def plural(word, lang):
    # pull language from culture?
    # lang.rule.plural
    pass
    
def random_name():
   name = [random.choice(adjective), random.choice(noun)]
   return name

"""def phoneme_fill(size):
    for s in size:
        random.randint"""

def describe(event):
    # construct narrative from event
    # there was a [great] [[snow]storm]] [last [year]]
    # usually [many] [people] [die], but not this time
    # the spirit [name] was [merciful]

    # the [animal] is [fierce], they are much more [powerful] than us
    # they [beat] [us] in [combat] the last [3] times!
    pass

class Story:
    def __init__(self, setting):#, protagonist, antagonist):
        #self.protagonist = protagonist
        #self.antagonist = antagonist
        self.setting = setting
        self.cast = setting.popList
        # Cast = [] instead of pro/antagonist

        self.conflict = "%s wants the %s %s, but %s" 
        # "%s needed the %s." % (protagonist, random.choice(noun))
        # def conflict(self, cast?
        # choose from popList
"""
class Numbers:
    def __init__(self, base):
        self.base = base
        	 can see 2 ways to accomplish
        	 making a sum of powers - elegante
        	 or like 
    base = 10
"""    

# TODO Prescriptive parser

"""def thus():
    
"""

# Syntax
# def statement(subject, object, verb):
#   identify pattern

# Grammar
# tense
# conjugation

# Number
# Ordinal
# Cardinal
# Base

# Sentence
#sentence = '%s %s %s. ' (noun[1], verb, noun)

"""print('Syllables:')
print(set(syllable))
print('Words:')
#print(set(word))
print(word)"""
#rudePhrase()
#print(random_name())
#print(sentence)

# Idosyncratics
# 
