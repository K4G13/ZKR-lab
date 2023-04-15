import imageio.v2 as iio
import numpy as np

img = iio.imread("secret.png")

for y in range(100):
    for x in range(100):
        pixel = img[y][x]
        if np.all(pixel == [255,255,255,255]):       
            print(".",end="")
        else:                      
            print("X",end="")
    print()
