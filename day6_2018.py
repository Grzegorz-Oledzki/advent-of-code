import numpy as np

with open ("test_input.txt", "r") as file:
    inputs = file.read().split("\n")
inputs = [x.split(", ") for x in inputs]

def get_input_coords(input):
    first_coord, second_coord = [], []
    for coord in inputs:
        first_coord.append(int(coord[0]))
        second_coord.append(int(coord[1]))
    return first_coord, second_coord

if __name__ == "__main__":

    area = np.zeros((10, 10))
    a, b = get_input_coords(inputs)
    area[1, 1] += 1
    for first_coord, second_coord in zip(a,b):
        area[first_coord:second_coord] += 1
    print(area)

