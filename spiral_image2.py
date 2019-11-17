from PIL import Image
import math as math
import random as rand

def spiral_image(name, red, green, blue, density=255, width=1000, height=1000):
    
    # Make the array of colours
    matrix = create_grid(width, height, red, green, blue)
    colours = grid_to_colours(matrix)

    # create the image
    img = Image.new('RGB', (width, height))
    img.putdata(colours)
    img.save(name)
    

def create_grid(width, height, red_max, green_max, blue_max):
    
    num_its = 2 * width * height
    d = 50  # density
    s = 10

    # make the pixel grid
    grid = [0] * height
    for i in range(height):
        grid[i] = [0] * width
    
    colours = [0] * (width*height)
    ymid = height // 2
    xmid = width // 2

    for t in range(num_its):
        # make the red spiral
        xr = round(t/d * math.cos(t/s)) + xmid
        yr = round(t/d * math.sin(t/s)) + ymid

        # make the blue spiral
        xb = round(math.cos(2*math.pi/3) * t/d * math.cos(t/s)) + xmid
        yb = round(math.sin(2*math.pi/3) * t/d * math.sin(t/s)) + ymid

        xg = round(-math.cos(2*math.pi/3) * t/d * math.cos(t/s)) + xmid
        yg = round(-math.sin(2*math.pi/3) * t/d * math.sin(t/s)) + ymid
        try:
            grid[xr][yr] = (red_max, 0, 0)
            grid[xb][yb] = (0, 0, blue_max)
            grid[xg][yg] = (0, green_max, 0)
        except IndexError:
            continue
    
    # probailistically fill the other pixels
    grid = zebra_fill(grid, red_max, green_max, blue_max)
    return grid

def melt_fill(matrix, red_max, green_max, blue_max):
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
                    choice = accumulate_colour(choices)
                else:
                    rnum = rand.randint(0,2)
                    if rnum == 0:
                        choice = (1, 1, blue_max)
                    elif rnum == 1:
                        choice = (red_max, 1, 1)
                    else:
                        choice = (1, green_max, 1)

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
                        choice = (1, 100, blue_max)
                    else:
                        choice = (red_max, 100, 1)
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
    colour = 

if __name__ == "__main__":
    spiral_image("spiral_image.png", 250, 250, 250)