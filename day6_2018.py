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

def ignore_infinite_coords(x_coord, y_coord):
    min_x, max_x, min_y, max_y = coords_limits(x_coord, y_coord)
    a = False
    if x_coord == min_x or x_coord == max_x or y_coord == min_y or y_coord == max_y:
        a = True
    return a

def get_distance_to_all_points(x_coords, y_coords):
    all_distances = []
    #min_x, max_x, min_y, max_y = coords_limits(x_coords, y_coords)
    coordinates = zip(x_coords, y_coords)
    for x_coord, y_coord in coordinates:
        distance = []
        # if x_coord == min_x or x_coord == max_x or y_coord == min_y or y_coord == max_y:
        #     continue
        for row_idx in range(10):
            for column_idx in range(10):
                distance.append(manhattan_distance(x_coord, y_coord, row_idx, column_idx))
        all_distances.append(distance)
    return all_distances

if __name__ == "__main__":



    x_coords, y_coords = get_input_coords(inputs)
    all_distances = get_distance_to_all_points(x_coords, y_coords)
    for distances in all_distances:
        closest_locations = 0
        for distance_idx, distance in enumerate(distances):
            count = 0
            for all_distances_index in range(1, len(all_distances)):
                #print(distance, all_distances[all_distances_index][distance_idx])
                if distance < all_distances[all_distances_index][distance_idx]:
                    count += 1
                if count == 5:
                    closest_locations += 1
        print(closest_locations)

        ##zrobic z tego funkcje ze daje sie jedne dystanse i porówna z wszystkimi innymi,
        # a jak bedzie 0 najbliższych pól to out







