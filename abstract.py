import numpy as np
import matplotlib.pyplot as plt
from random import randrange

width = 800
height = 600
canvas = np.zeros((height, width, 3), dtype=np.uint8)


one= randrange(255)
two = randrange(255)
three = randrange(255)

for x in range(width):
    canvas[:, x] = [x / width * one, two, (1 - x / width) * three]
    
plt.imshow(canvas)
plt.axis('off')
plt.savefig('image.jpg', bbox_inches='tight', pad_inches=0, dpi=300)
plt.show()