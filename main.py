import dictionary as dic
#import setting_synth
from battle import *
from number_base import *
import place, entities
import display
from generators import *

gameState = 1
pause = True
event_log = []

pop = 5
town = Location('town', 500, pop)
fillLocation(town)
language = randomLanguage()
print(language.vowels, language.consonants)
print(language.words)

#print(town.name, town.list)
#town.census()





### Branching save narrative wxploration
