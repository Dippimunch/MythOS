import XSAMPA as xsam
import numpy as np
from numpy import random
import random, math
from PIL import Image
from scipy.ndimage.filters import gaussian_filter
from generators import generate_perlin_noise_2d

height = 1024
width = 720
temp_map = np.empty((height, width))
perlin = generate_perlin_noise_2d((height, width), (2, 2))

# Sine shit
t = 10
amp = 10000
freq = 10
omega = 2 * np.pi * freq

def gen_syll_struct():
    struct_type = ''
    r = random.randrange(0, 458)
    if r <= 60:
        struct_type = 'simple'
    elif r > 60 and r <= 273:
        struct_type = 'moderately complex'
    else:
        struct_type = 'complex'

    return struct_type
    

# temp_map = random.randint(100, size=(height,width))
def gen_map(map_array, height, width):
    for h in range(height):
        for w in range(width):

            temp_map[h][w] = random.gauss(50, 17)

    im = Image.fromarray(perlin, mode='RGB')
    im_gauss = Image.fromarray(gaussian_filter(temp_map, sigma=3))

    if im.mode != 'L':
        im = im.convert('L')

    if im_gauss.mode != 'RGB':
        im_gauss = im_gauss.convert('RGB')
    def save(image):
        image.save("temp_map.png")
        #image.gauss().save("temp_map_gauss.png")

    save(im)

#print(generate_perlin_noise_2d((10, 10), (2, 2)))
#print(temp_map)
#print(gaussian_filter(temp_map, sigma=3))

"""for i in range(t):
    print(amp * np.sin(omega * i) + 1, i)"""

print(gen_syll_struct(), gen_syll_struct(), gen_syll_struct(), gen_syll_struct(), gen_syll_struct())
    
