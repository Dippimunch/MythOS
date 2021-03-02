import math
import random


temp_min = 0
temp_max = 100

samples = 360
s = 0

# Tempeture range
amplitude = 50
# Length of year
period = 360
# Temperature at beginning of year
phase = 0
# Midpoint
vertical = 50

location = None

def class Climate:
    def __init__(self, name, amplitude, period, phase, vertical):
        pass

def get_weather(location, amplitude, period, phase, vertical, time):
    variation = random.randrange(-20, 20)
    temp = amplitude * math.sin((2*math.pi/period)*(time-phase)) + vertical
    return temp + variation
    
while s < samples:
    print(get_weather(location, amplitude, period, phase, vertical, s))
    s += 1
