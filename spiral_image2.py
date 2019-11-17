from PIL import Image
import math as math
import random as rand

def spiral_image(name, red, green, blue, density=10, tightness=50, width=1000, height=1000):
    
    # Make the array of colours
    matrix = create_grid(width, height, density, tightness, red, green, blue)
    colours = grid_to_colours(matrix)

    # create the image
    img = Image.new('RGB', (width, height))
    img.putdata(colours)
    img.save(name)
    

def create_grid(width, height, density, tightness, red_max, green_max, blue_max):
    
    num_its = 2 * width * height
    d = density  # density controls how short the steps between values are
    s = tightness # tightness controls how short fast the spiral unwinds

    base_one = (255, 140, 0)
    base_two = (0, 0, 128)
    base_three = (220, 20, 60)


    # make the pixel grid
    grid = [0] * height
    for i in range(height):
        grid[i] = [0] * width
    
    colours = [0] * (width*height)
    ymid = height // 2
    xmid = width // 2

    for t in range(num_its):
        # make the red spiral
        xbase = round(t/d * math.cos(t/s))
        ybase = round(t/d * math.sin(t/s))

        xr = round(t/d * math.cos(t/s)) + xmid
        yr = round(t/d * math.sin(t/s)) + ymid

        # make the blue spiral
        ang = 2 * math.pi/3
        xb = round(math.cos(ang) * xbase  - math.sin(ang) * ybase) + xmid
        yb = round(math.sin(ang) * xbase + math.cos(ang) * ybase) + ymid

        # make the green spiral
        xg = round(math.cos(-1*ang) * xbase  - math.sin(-1*ang) * ybase) + xmid
        yg = round(math.sin(-1*ang) * xbase + math.cos(-1*ang) * ybase) + ymid
        
        # put the colours in
        try:
            grid[xr][yr] = base_one
            grid[xb][yb] = base_two
            grid[xg][yg] = base_three
        except IndexError:
            continue
    
    # probailistically fill the other pixels
    grid = melt_fill(grid, base_one, base_two, base_three)
    return grid

def melt_fill(matrix, base_one, base_two, base_three):
    grid = matrix.copy()
    width = len(matrix)
    height = len(matrix[0])
    for i in range(width):
        for j in range(height):
            # let's probabilistically decide the colour
            # We look at the surrounding pixels and make the best guess
            if grid[i][j] == 0:
                choices = []
                for k in range(8):
                    xplus = round(math.cos(k * math.pi/8))
                    yplus = round(math.sin(k * math.pi/8))
                    try:
                        if grid[i + xplus][j + yplus] != 0:
                            choices.append(grid[i + xplus][j + yplus])
                    except IndexError:
                        continue
                if len(choices) != 0:
                    grid[i][j] = accumulate_colour(choices)
                else:
                    rnum = rand.randint(0,2)
                    if rnum == 0:
                        grid[i][j] = base_one
                    elif rnum == 1:
                        grid[i][j] = base_two
                    else:
                        grid[i][j] = base_three
    return grid

def zebra_fill(matrix, red_max, green_max, blue_max):
    grid = matrix.copy()
    width = len(matrix)
    height = len(matrix[0])
    for i in range(width):
        for j in range(height):
            # let's probabilistically decide the colour
            # We look at the surrounding pixels and make the best guess
            if grid[i][j] == 0:
                choices = []
                for k in range(8):
                    xplus = round(math.cos(k * math.pi/8))
                    yplus = round(math.sin(k * math.pi/8))
                    try:
                        if grid[i + xplus][j + yplus] != 0:
                            choices.append(grid[i + xplus][j + yplus])
                    except IndexError:
                        continue
                if len(choices) != 0:
                    choice = choices[rand.randint(0, len(choices) - 1)]
                    grid[i][j] = choice
                else:
                    rnum = rand.randint(0,1)
                    if rnum == 0:
                        grid[i][j] = (1, 100, blue_max)
                    else:
                        grid[i][j] = (red_max, 100, 1)
    return grid

def grid_to_colours(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    colours = [0] * (num_rows * num_cols)

    # For each row
    for i in range(len(matrix)):
        # For each column
        for j in range(len(matrix[0])):
            colours[(i * num_rows) + j] = matrix[i][j]
    
    return colours

def accumulate_colour(colour_list):
    colour = (0, 0, 0)
    n = len(colour_list)
    # add all the colours together
    for col in colour_list:
        colour = tuple(map(sum, zip(colour, col)))

    # get an average colour
    #colour = (max(round(colour[0]/n),250), max(round(colour[1]/n), 250), max(round(colour[2]/n), 250))
    colour = (round(colour[0]/n), round(colour[1]/n), round(colour[2]/n))

    return colour


if __name__ == "__main__":
    spiral_image("spiral_image.png", 0, 250, 250, 1, 100)