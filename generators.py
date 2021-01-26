import dictionary as dic
import random
from entities import *

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
    cons = []
    vowels = []
    
    c_chart = dic.consonant_chart()
    c_choice = None

    name = 'Name'

    for c in range(len(c_chart)):
        if c < con_num:
            c_choice = random.randrange(len(c_chart))
            cons.append(c_chart[c_choice])
            c_chart.remove(c_chart[c_choice])

    return Language(name, cons, [], [])    
        
language = randomLanguage()
print(language.consonants)

# generalize
#def town():
#   print(dic.pick('pronoun' or 'verb'))

    
