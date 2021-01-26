import dictionary as dic
from entities import *

strings = ['in a time before time', 'long ago', 'when all was naught but light']




def fillLocation(location):
    for p in range(location.population):
        person = Person(p, 20)
        location.list.append(person)

def makePerson():
    pass
        
def randomLanguage():
    pass

print(dic.consonant_chart())
    
# generalize
#def town():
#   print(dic.pick('pronoun' or 'verb'))

    
