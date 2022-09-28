import dictionary as dic
from generators import randomLanguage


language = randomLanguage()
tense = 'past'
character_1 = {'name': 'John','sex': 'male'}
character_2 = {'name': 'Death','sex':  'female'}
item_1 = 'scythe'

# LInguistic Gloss
# There once lived a happy, rich man whose name was John
atu_899 = [['there', 'is', character_1['name'], 'live'], [character_1['name'], 'has', 'all'],
           [character_1['name'], 'has', 'many', 'horses', 'cattle', 'friends', 'good', 'wife', 'money'],
           ['a', 'day', character_2['name'], 'come', 'to', 'door', 'knock'],
           ['when', character_1['name'], 'open', 'door', character_2['name'], 'stand', 'with', item_1, 'on', 'back'],
           [character_2['name'], 'say', 'hello', 'boy', 'come', 'with', 'me', 'is', 'time', 'go'],
           [character_1['name'], 'is', 'afraid', character_2['name']],
           [character_1['name'], 'begin', 'cry', 'and', 'beg', 'life']]

print(dic.translate('ice', language))
