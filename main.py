from re import T
from PIL import Image
from classes import Square, Grid
from os import listdir
from random import randint
import json

def image_grid(squares, size):
    assert len(squares) == size**2

    w, h = squares[0].image.size
    grid = Image.new('RGB', size=(size*w, size*h))

    
    for i, square in enumerate(squares):
        grid.paste(square.image, box=(i%size*w, i//size*h))
    return grid

def update_grid(full_grid, obj, size):

    width = obj.width
    height = obj.height

    index = height * size + width

    if width > 0:
        left = full_grid[index - 1]
        left.options = update_options(left, 1, obj.square.rules[3])

    if width < size - 1:
        right = full_grid[index + 1]
        right.options = update_options(right, 3, obj.square.rules[1])

    if height > 0:
        up = full_grid[(height - 1) * size + width]
        up.options = update_options(up, 2, obj.square.rules[0])

    if height < size - 1:
        down = full_grid[(height + 1) * size + width]
        down.options = update_options(down, 0, obj.square.rules[2])


def update_options(grid, side, value):
    new_options = []
    for option in grid.options:
        if option.rules[side] == value:
            new_options.append(option)

    return new_options

def algorithm(squares, size):

    object_grid = [Grid(squares, i%size, i//size) for i in range(size**2)]
    w, h = squares[0].image.size
    grid = Image.new('RGB', size=(size*w, size*h))


    for i in range(size ** 2):
        grid_sorted = sorted(object_grid, key=lambda x: len(x.options))
        for obj in grid_sorted:
            if obj.collapsed == False:
                choice = randint(0, len(obj.options)-1)
                square = obj.options[choice]
                
                obj.square = square
                obj.collapsed = True
                obj.options = []

                update_grid(object_grid, obj, size)

                break

        
        #grid.show()

    #Update options of neighbors
    for i, obj in enumerate(object_grid):
        grid.paste(obj.square.image, box=(obj.width*w, obj.height*h))

    grid.show(title = "map")
    
def get_rules(file):

    f = open(file)
    data = json.load(f)
    f.close()
    return data

def rotate_rules(rules, num_rotations):

    new_rules = [0 for elem in rules]

    for i in range(len(rules)):
        new_rules[i] = rules[(num_rotations + i) % 4]
        #print(rules, new_rules, i, (num_rotations + i) % 4)

    return new_rules

def create_squares(images_folder, rules_file):

    rules = get_rules(rules_file)

    squares = []

    for file_name in listdir(images_folder):
        image_rules = rules[file_name]
        for id_rotated in range(4):
            im = Image.open(images_folder + file_name)

            im = im.rotate(90 * id_rotated)
            new_rules = rotate_rules(image_rules, id_rotated)

            new = Square(im, file_name, id_rotated, new_rules)
            squares.append(new)

    return squares


if __name__ == '__main__':

    size = 40
    test = "tubes"
    images_folder = f"./images/{test}/"
    rules_file = f"./rules/{test}.json"

    squares = create_squares(images_folder, rules_file)


    while True:
        algorithm(squares, size)
        x = input()
    #grid = image_grid(squares, size)
    #grid.show()
    