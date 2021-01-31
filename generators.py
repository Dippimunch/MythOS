import dictionary as dic
import random
from entities import *
import XSAMPA as xsam



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

    vowels = []
    v_choice = None

    cons = []
    c_choice = None

    name = 'Name'

    for v in range(vowel_num):
        v_choice = random.choice(v_chart)
        vowels.append(v_choice)
        v_chart.remove(v_choice)

    for c in range(con_num):
        c_choice = random.choice(c_chart)
        cons.append(c_choice)
        c_chart.remove(c_choice)

    """for c in range(len(c_chart)):
        if c < con_num:
            c_choice = random.randrange(len(c_chart))
            cons.append(c_chart[c_choice])
            c_chart.remove(c_chart[c_choice])"""

    return Language(name, cons, vowels, None)    
        
#print(language.consonants)

# generalize
#def town():
#   print(dic.pick('pronoun' or 'verb'))

    
