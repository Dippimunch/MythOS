import math
import random, re
import numpy as np


temp_min = 0
temp_max = 100

samples = 20
s = 0

# day to begin
time = 50

# Tempeture range
amplitude = 50
# Length of year
period = 360
# Temperature at beginning of year
phase = 0
# Midpoint
vertical = 50
# TODO: Latitude/ geographic variation

location = None

# Whittaker classification precipitation/temperature


# Holdridge life zome
#h_biome = {

### Koppen climate classification
koppen_cat = {'Group':{'A':'Tropical', 'B':'Dry', 'C':'Temperate', 'D':'Continental', 'E':'Polar'},
              'Precipitaion':{'A':{'f':'Rainforest', 'm':'Monsoon', 'w':'Savanna, Dry winter', 's':'Savanna, Dry summer'},
                              'B':{'w':'Desert', 's':'Steppe'},
                              'C':{'w':'Dry winter', 'f':'No dry season', 's':'Dry summer'},
                              'D':{'w':'Dry winter', 'f':'No dry season', 's': 'Dry summer'},
                              'E':{'T': 'Tundra', 'F': 'Eternal frost'}},
              'Temperature':{'A':{None},
                              'B':{'h':'Hot', 'k':'Cold'},
                              'C':{'a':'Hot summer', 'b':'Warm summer', 'c':'Cold summer'},
                              'D':{'a':'Hot summer', 'b':'Warm summer', 'c':'Cold summer', 'd':'Very cold wimter'},
                             'E': None}}              

class Climate:
    def __init__(self, name, temp_range, period, phase, vertical, ev_rate):
        self.name = name
        self.temp_range = temp_range
        self.period = period
        self.phase = phase
        self.vertical = vertical
        self.ev_rate = ev_rate

        # Koppen reader
        def clasf(koppen_cat):
            pass

def get_weather(location, amplitude, period, phase, vertical, time):
    variation = math.floor(np.random.normal(0, .05)*50)
    print('var: ' + str(variation))
    temp = amplitude * math.sin((2*math.pi/period)*(time-phase)) + vertical
    return round(temp + variation)

location = Climate('Location', 50, 360, 0, 50, 1)

"""while s < samples:
    print(get_weather(location, amplitude, period, phase, vertical, time))
    time += 1
    s += 1"""
