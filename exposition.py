from entities import *
import dictionary as dic
from generators import *


date = 0
language = randomLanguage()
location = Location('home', 1000, 'CCf', 100)
player = Person('Name', 25, 'M', language, {}, location)
print(f'you are with your kinfolk at {player.location.name}')
#print(language.__dict__)
print(dic.translate(f'you be with your human at {player.location.name}', language))
dic.read_xsampa('R*aLRML')
# 2ndPerson be LOCATION locative KIN comitative


# 2ndPerrsonPossesive how to do cases generatively?
# just gonna hardcode for now
