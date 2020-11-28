import random
import numpy
from tcod.libtcod import ffi, lib
import tcod.constants

#myname = tcod.namegen_generate("a")
#print(myname)

generator = tcod.random.Random()
#print(tcod.random.gauss(5, 5))

def generations(count, avg_age, rnd):
    lineage = []
    age = 0
    for gen in range(count):
        variation = tcod.random_get_int_mean(rnd, -4, 30, 1)
        lineage.append(avg_age + variation)
        age += lineage[gen]
    print(lineage)
    return lineage
    #print(lineage, age)

f = open('generations.txt', 'w+')
lineage = ''.join(generations(100, 20, generator))
f.write(lineage)
f.close()


### https://python-tdl.readthedocs.io/en/stable/libtcodpy.html
