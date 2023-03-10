import dictionary as dic
#import setting_synth
from battle import *
from number_base import *
import entities
from generators import *
from display import *

game_state = 1
pause = True
event_log = []

pop = 5
town = Location('town', 500, 'Cfb', pop)
fillLocation(town)
#language = randomLanguage()
#print(language.vowels, language.consonants)
#print(lang uage.words)
#print(dic.translate('human drink 20 water',language))

#print(town.name, town.list)
#town.census()



menu = Menu('MAIN', ['new', 'load', 'print', 'exit'])

if game_state == 1:
    action = input(menu.display())

    if action == 1:
        pass
        # initialization
    if action == 2:
        pass
    if action == 3:
        print("PRINT")
    if action == 4:
        print('Really quit? y/n')
        if action == 'y':
            exit()
    else:
        print(action)
        # return


