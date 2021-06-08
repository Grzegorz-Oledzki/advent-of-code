import numpy as np

with open ("test_input.txt", "r") as file:
    inputs = file.read().split("\n")
inputs = [x.split(", ") for x in inputs]

def get_input_coords(input):
    first_coord, second_coord = [], []
    for coord in inputs:
        second_coord.append(int(coord[0]))
        first_coord.append(int(coord[1]))
    return first_coord, second_coord

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def coords_limits(x_coord, y_coord):
    min_x, max_x = min(x_coord), max(x_coord)
    min_y, max_y = min(y_coord), max(y_coord)
    return min_x, max_x, min_y, max_y

# def ignore_infinite_coords():
#     if x_coord == min_x or x_coord == max_x or y_coord == min_y or y_coord == max_y:
#         True


if __name__ == "__main__":

    area = np.zeros((10, 10))

    x_coords, y_coords = get_input_coords(inputs)

    coordinates = zip(x_coords, y_coords)

    min_x, max_x, min_y, max_y = coords_limits(x_coords, y_coords)
    print(min_x, max_x, min_y, max_y)
    for x_coord, y_coord in coordinates:
        distance = []
        if x_coord == min_x or x_coord == max_x or y_coord == min_y or y_coord == max_y:
            continue
        for row_idx in range(10):
            for column_idx in range(10):
                distance.append(manhattan_distance(x_coord, y_coord, row_idx, column_idx))
        print(x_coord, y_coord, distance)




