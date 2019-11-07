"""
First ever image
Make a cool chaotically generated image
"""

from PIL import Image
import math as math
import random as rand


"""
Function to generate the cascading images
"""
def make_cascade(name, red, green, blue, density=255, width=1000, height=1000):

    width
    height
    colours = [None] * (width*height)

    # First let's set the top row of pixels
    for i in range(width):
        colours[i] = (i % density, 0, 0)

    # Now let's set the future row's of pixels    
    for i in range(width*(height - 1)):
        # we want to base colour choices on what the pixels above are
        # create a series of colour choices
        # make an array for the options of next pixel
        start = max(0, i - 3)
        end = i + 3
        choices = [0] * (end - start)
        for k in range(end - start):
            choices[k] = colours[start + k]

        choice = rand.randint(0, end - start - 1)
        shift = (i + width) / (width*height)
        colour = choices[choice][0]      
        colours[width + i] = (colour, math.floor(shift * green), math.floor(shift*blue))
        #my_list[i] = (math.floor(255/i), math.floor(), i%2)

    img = Image.new('RGB', (width, height))
    img.putdata(colours)
    img.save(name)

make_cascade('image.png', 100, 31, 89, 255)
