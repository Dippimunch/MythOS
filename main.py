import dictionary as dic
#import setting_synth
from battle import *
from number_base import *
import entities, display
from generators import *

game_state = 1
pause = True
event_log = []

pop = 5
town = Location('town', 500, 'Cfb', pop)
fillLocation(town)
language = randomLanguage()
#print(language.vowels, language.consonants)
#print(language.words)
#print(dic.translate('human drink 20 water',language))

#print(town.name, town.list)
#town.census()

if game_state == 1:
    print('actions')
    action = input()
