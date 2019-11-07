from PIL import Image
import math as math
import random as rand


"""
Make the fibonacci numbers
"""
def make_fibs(n):
    fib_list = [0] * n
    fib_list[1] = 1
    for i in range(2, n):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list

fib_list = make_fibs(1000)

"""
Makes an image where the RGB colours are determined by functions
"""
def functional_image(name, red, green, blue, density=255, width=1000, height=1000):
    
    # make the pixel grid
    grid = [0] * height
    for i in range(height):
        grid[i] = [0] * width

    # Make the array of colours
    colours = create_colours(grid, width, height, red, green, blue)

    # create the image
    img = Image.new('RGB', (width, height))
    img.putdata(colours)
    img.save(name)
    
"""
Get the colours for the image using different functions
"""
def create_colours(grid_matrix, width, height, red_max, green_max, blue_max):
    colours = [0] * (width*height)
    hmid = height // 2
    wmid = width // 2
    k = 0
    for j in range(height):
        for i in range(width):
            # Make the coordinates
            y = hmid - j
            x = i - wmid

            # Get each colour value
            rval = red_function(x, y, red_max)
            gval = green_function(x, y, green_max)
            bval = blue_function(x, y, blue_max)

            # Put the colour values in an array
            colour = (rval, gval, bval)
            colours[k] = colour
           
            k += 1
    
    return colours 

"""
Generate the red colour
"""
def red_function(x, y, red_max):
    return rand.randint(0, red_max)

    #return math.floor(math.sin((math.sqrt(x*x + y*y))) * red_max) 
    #return math.floor(math.sin(x+y) * red_max)

"""
Generate the green colour
"""
def green_function(x, y, green_max):
    
    return 0

    #return math.floor(rand.randint(0,1) * green_max)
    #return (abs(x-y) + abs(x+y) + max(abs(x),abs(y))) % green_max 

"""
Generate the blue colour
"""
def blue_function(x, y, blue_max):

    return 0
    

    # return fib_list[math.floor(math.sqrt(x*x + y*y))] % blue_max
    # index = math.floor(math.sqrt(x*x + y*y))
    # fib_max = fib_list[len(fib_list) - 1]
    # if index == 0:
    #     return 0
    # return math.floor((index/fib_list[index])  *  blue_max) 



functional_image("fimage.png", 255, 50, 255)