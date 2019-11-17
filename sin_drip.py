from PIL import Image
import math as math
import random as rand
from spiral_image2 import grid_to_colours


"""
Function to generate the cascading images
"""
def sin_drip(name, red, green, blue, density=255, width=1000, height=1000):

    max_wobble = 200
    num_periods = 12

    # make the pixel grid
    grid = [0] * height
    for i in range(height):
        grid[i] = [0] * width

    colours = [None] * (width*height)

    # First let's set the top row of pixels
    for i in range(width):
        grid[0][i] = (i % red, i % green, i % blue)

    # Now let's set the future row's of pixels    
    for i in range(1, width):
        for j in range(height):
        # we want to base colour choices on what the pixels above are
        # create a series of colour choices
        # make an array for the options of next pixel
            start = max(0, j - 3)
            end = min(j+3, height-1)
            choices = []
            for k in range(end - start):
                choices.append(grid[i-1][start + k])

            choice = rand.randint(0, end - start - 1)
            
            # sin wobble part
            # we use -k to make a symmetric effect occur
            k = (j + round(math.exp(i * math.log(max_wobble)/1000) * math.sin(math.pi * 2 * num_periods * i / height)))%height
            grid[i][-k] = choices[choice]
    
            

    colours = grid_to_colours(grid)
        
    img = Image.new('RGB', (width, height))
    img.putdata(colours)
    img.save(name)


def sin_drip_base_colours(name, red, green, blue, density=255, width=1000, height=1000):

    max_wobble = 200
    num_periods = 13

    # make the pixel grid
    grid = [0] * height
    for i in range(height):
        grid[i] = [0] * width

    colours = [None] * (width*height)

    base_one = (135, 206, 350)
    base_two = (255, 255, 0)
    base_three = (255, 99, 71)

    # First let's set the top row of pixels
    for i in range(width):
        if i%3 == 0:
            grid[0][i] = base_one
        elif i%3 == 1:
            grid[0][i] = base_two
        else:
            grid[0][i] = base_three 

    # Now let's set the future row's of pixels    
    for i in range(1, width):
        for j in range(height):
        # we want to base colour choices on what the pixels above are
        # create a series of colour choices
        # make an array for the options of next pixel
            start = max(0, j - 3)
            end = min(j+3, height-1)
            choices = []
            for k in range(end - start):
                choices.append(grid[i-1][start + k])

            choice = rand.randint(0, end - start - 1)
            
            # sin wobble part
            # we use -k to make a symmetric effect occur 
            #k = (j + round(100 * math.sin(math.pi * 2 * num_periods * i / height)))%height   # this is for no decay
            k = (j + round(math.exp((width - i) * math.log(max_wobble)/1000) * math.sin(math.pi * 2 * num_periods * i / height)))%height # this is with decay
            grid[i][-k] = choices[choice]
    
            

    colours = grid_to_colours(grid)
        
    img = Image.new('RGB', (width, height))
    img.putdata(colours)
    img.save(name)


if __name__ == "__main__":
    #sin_drip('sin_drip.png', 65, 105, 225)
    sin_drip_base_colours('sin_drip_bc.png', 0, 0, 0)
