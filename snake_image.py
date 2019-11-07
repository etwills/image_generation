from PIL import Image
import math as math
import random as rand


"""
Makes an image where the RGB colours are determined by functions
"""
def snake_image(name, red, green, blue, density=255, width=1000, height=1000):
    

    # Make the array of colours
    colours = create_colours(width, height, red, green, blue)

    # create the image
    img = Image.new('RGB', (width, height))
    img.putdata(colours)
    img.save(name)
    
"""
Get the colours for the image using different functions
"""
def create_colours(width, height, red_max, green_max, blue_max):
    
    # make the pixel grid
    grid = [0] * height
    for i in range(height):
        grid[i] = [0] * width
    
    colours = [0] * (width*height)
    hmid = height // 2
    wmid = width // 2
    
    max_count = 0
    dirx = 0
    diry = 0
    for k in range(math.floor(height/2)):
        x = 0
        y = 0
        if k % 4 == 0:
            dirx = 1
            diry = 1
        elif k % 4 == 1:
            dirx = -1
            diry = 1
        elif k % 4 == 2:
            dirx = -1
            diry = 1
        else:
            dirx = 1
            diry = -1
        
        # Run a snaking path through the image
        for i in range(width * 10):
            grid[y + hmid][x + wmid] = k
            #grid[y + hmid][x + wmid] = grid[y + hmid][x + wmid] + k
            
            # change the maximum
            if grid[y+hmid][x+wmid] > max_count:
                max_count = grid[y+hmid][x+wmid]

            # Change the direction of the paths
            x += dirx
            y += diry
            
            # Break out if we reach the edge
            if x + wmid < 0 or x + wmid >= width:
                break
            if y + hmid < 0 or y + hmid >= height:
                break

            dirx = change_sign(dirx)
            diry = change_sign(diry)

    print(max_count)
    k = 0
    for j in range(height):
        for i in range(width):

            # Get each colour value
            rval = grid[j][i] % red_max
            gval = grid[j][i] % green_max
            # gval = math.floor((grid[j][i]/max_count) * green_max)
            bval = grid[j][i] % blue_max
            # rval = math.floor((grid[j][i]/max_count) * red_max)
            # gval = 50
            # # gval = math.floor((grid[j][i]/max_count) * green_max)
            # bval = math.floor((grid[j][i]/max_count) * blue_max)


            # Put the colour values in an array
            colour = (rval, gval, bval)
            colours[k] = colour
           
            k += 1
    
    return colours 

# """
# Generate the red colour
# """
# def red_function(x, y, red_max):
#     return rand.randint(0, red_max)

#     #return math.floor(math.sin((math.sqrt(x*x + y*y))) * red_max) 
#     #return math.floor(math.sin(x+y) * red_max)

# """
# Generate the green colour
# """
# def green_function(x, y, green_max):
    
#     return 0

#     #return math.floor(rand.randint(0,1) * green_max)
#     #return (abs(x-y) + abs(x+y) + max(abs(x),abs(y))) % green_max 

# """
# Generate the blue colour
# """
# def blue_function(x, y, blue_max):

#     return 0
    

#     # return fib_list[math.floor(math.sqrt(x*x + y*y))] % blue_max
#     # index = math.floor(math.sqrt(x*x + y*y))
#     # fib_max = fib_list[len(fib_list) - 1]
#     # if index == 0:
#     #     return 0
#     # return math.floor((index/fib_list[index])  *  blue_max) 

def change_sign(val):
    if rand.random() <= 0.85:
        return val
    else:
        return val * -1

snake_image("fimage.png", 251, 137, 159)