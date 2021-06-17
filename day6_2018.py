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


def coords_limits(x_coords, y_coords):
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    return min_x, max_x, min_y, max_y


def get_distance_to_all_points(x_coords, y_coords):
    all_distances = []
    coordinates = zip(x_coords, y_coords)
    for x_coord, y_coord in coordinates:
        distance = []
        for row_idx in range(max(x_coords)):
            for column_idx in range(max(y_coords)):
                distance.append(manhattan_distance(x_coord, y_coord, row_idx, column_idx))
        all_distances.append(distance)
    return all_distances


def get_number_of_closest_points(all_distances,distances):
    closest_points = 0
    for distance_idx, distance in enumerate(distances):
        count = 0
        for all_distances_index in range(len(all_distances)):
            if distance < all_distances[all_distances_index][distance_idx]:
                count += 1
            if count == len(all_distances)-1:
                closest_points += 1
    return closest_points


def get_all_numbers_of_closest_points(all_distances):
    numbers_of_closest_points = []
    for distances_index in range(len(all_distances)):
        numbers_of_closest_points.append(get_number_of_closest_points(all_distances,all_distances[distances_index]))
    return numbers_of_closest_points


def get_finite_coords(coords):
    min_x, max_x, min_y, max_y = coords_limits(x_coords, y_coords)
    finite_coords = []
    for x_coord, y_coord in coords:
        if x_coord == min_x or x_coord == max_x or y_coord == min_y or y_coord == max_y:
            continue
        else:
            finite_coords.append((x_coord, y_coord))
    return finite_coords

#def find_numbers_of_closest_points_finite_coords(finite_coords):




if __name__ == "__main__":

    x_coords, y_coords = get_input_coords(inputs)
    all_distances = get_distance_to_all_points(x_coords, y_coords)
    all_numbers_of_closest_points = get_all_numbers_of_closest_points(all_distances)
    coords = zip(x_coords, y_coords)

    print(all_numbers_of_closest_points)











