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
    
    num_its = 10000
    d = 25  # density
    s = 100

    # make the pixel grid
    grid = [0] * height
    for i in range(height):
        grid[i] = [0] * width
    
    colours = [0] * (width*height)
    ymid = height // 2
    xmid = width // 2

    for t in range(num_its):
        # make the red spiral
        xr = round((t/d * math.cos(t/s))) + xmid
        yr = round((t/d * math.sin(t/s))) + ymid
        grid[xr][yr] = (red_max, 100, 0)

        # make the blue spiral
        xb = round((-t/d * math.cos(t/s))) + xmid
        yb = round((-t/d * math.sin(t/s))) + ymid
        grid[xb][yb] = (0, 100, blue_max)
    
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


def blue(x, y, blue_max):
    return math.sin(math.atan(y/x)) * (math.sqrt(x*x + y*y))  # r*sin(theta)

def red(x, y, red_max):
    return -1 * math.sin(math.atan(y/x)) * (math.sqrt(x*x + y*y))  # -r*sin(theta)


if __name__ == "__main__":
    spiral_image("spiral_image.png", 250, 137, 250)