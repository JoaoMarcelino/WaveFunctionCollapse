from PIL import Image
from square import Square
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

def algorithm(squares, size):

    fill_grid = [[0] * size for a in range(size)]
    
    w, h = squares[0].image.size
    grid = Image.new('RGB', size=(size*w, size*h))

    index = randint(0, len(squares)-1)

    square = squares[index]

    grid.paste(square.image, box=(0, 0))

    



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

    grid = image_grid(squares, size)
    grid.show()
    