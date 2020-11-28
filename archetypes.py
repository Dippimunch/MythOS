import random


ego = ['The Innocent', 'The Orphan', 'The Hero', 'The Caregiver']
soul = ['The Explorer', 'The Rebel', 'The Lover', 'The Creator']
self = ['The Jester', 'The Sage', 'The Magician', 'The Ruler']

archetype = [ego, soul, self]

def rand_arch():
    x = random.randrange(2)
    y = random.randrange(3)
    
    return archetype[x][y]

print(rand_arch())
    
