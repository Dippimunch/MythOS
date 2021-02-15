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
eng_lang = Language('English', ['p', 'b', 't', 'd', 'ts', 'dz', 'k', 'g', 'f',
                                'v', 'T', 'D', 's', 'z', 'S', 'Z', 'h', 'm', 'n',
                                'N', 'l', 'r', 'w', 'w'],
                                ['A:', 'i:', 'I', 'E', '3:', '{', 'A:', 'V', 'Q',
                                 'O:', 'U', 'u:', '@'], 10, dic.swadesh)
#print(language.vowels, language.consonants)
#print(language.words)
#print('base: ', language.base)
print(dic.translate('human drink water',language))

#print(town.name, town.list)
#town.census()
