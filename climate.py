import math


temp_min = 0
temp_max = 100

samples = 180
s = 0

location = None

def get_weather(location, time):
    #print(math.sin(time))
    #temp = (temp_max/2) * math.sin(time)
    #print(math.radians(1))
    temp = 50 * math.sin(math.radians(time))
    return temp
    
while s < samples:
    print(get_weather(location, s))
    s += 1
