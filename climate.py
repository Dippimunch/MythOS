import math
import random
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

class Climate:
    def __init__(self, name, amplitude, period, phase, vertical):
        pass

def get_weather(location, amplitude, period, phase, vertical, time):
    variation = math.floor(np.random.normal(0, .05)*50)
    print('var: ' + str(variation))
    temp = amplitude * math.sin((2*math.pi/period)*(time-phase)) + vertical
    return round(temp + variation)
    
while s < samples:
    print(get_weather(location, amplitude, period, phase, vertical, time))
    time += 1
    s += 1
