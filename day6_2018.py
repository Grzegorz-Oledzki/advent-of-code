with open("input6.txt", "r") as file:
    inputs = file.read().split("\n")
inputs = [x.split(", ") for x in inputs]


def get_input_coords(inputs):
    first_coord, second_coord = [], []
    for coord in inputs:
        second_coord.append(int(coord[1]))
        first_coord.append(int(coord[0]))
    return first_coord, second_coord


def manhattan_distance(x_coord, y_coord, row_idx, column_idx):
    return abs(x_coord - row_idx) + abs(y_coord - column_idx)


def coords_limits(x_coords, y_coords):
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    return min_x, max_x, min_y, max_y


def get_distance_to_all_points(x_coords, y_coords):
    all_distances = []
    all_x_coords = []
    all_y_coords = []
    for x_coord, y_coord in zip(x_coords, y_coords):
        distance = []
        for row_idx in range(max(x_coords)):
            for column_idx in range(max(y_coords)):
                distance.append(
                    manhattan_distance(x_coord, y_coord, row_idx, column_idx)
                )
                all_x_coords.append(row_idx)
                all_y_coords.append(column_idx)
        all_distances.append(distance)
    return all_distances, all_x_coords, all_y_coords


def get_number_of_closest_points_and_check_if_coord_is_finite(
    all_distances,
    all_x_coords,
    all_y_coords,
    distances,
    x_coords,
    y_coords,
    distances_index,
):
    min_x, max_x, min_y, max_y = coords_limits(x_coords, y_coords)
    closest_points = 0
    finest_point = []
    x_coords_of_the_nearest_points, y_coords_of_the_nearest_points = [], []
    for distance_idx, distance in enumerate(distances):
        count = 0
        for all_distances_idx in range(len(all_distances)):
            if distance < all_distances[all_distances_idx][distance_idx]:
                count += 1
                if count == len(all_distances) - 1:
                    closest_points += 1
                    x_coords_of_the_nearest_points.append(all_x_coords[distance_idx])
                    y_coords_of_the_nearest_points.append(all_y_coords[distance_idx])
    if (
        min_y not in x_coords_of_the_nearest_points
        and max_y not in x_coords_of_the_nearest_points
        and min_x not in y_coords_of_the_nearest_points
        and max_x not in y_coords_of_the_nearest_points
    ):
        finest_point.append((x_coords[distances_index], y_coords[distances_index]))
    return closest_points, finest_point


def get_all_numbers_of_closest_points(
    all_distances, x_coords, y_coords, all_x_coords, all_y_coords
):
    numbers_of_closest_points = []
    finite_coords = []
    for distances_index in range(len(all_distances)):
        closest_point, finite_coord = get_number_of_closest_points_and_check_if_coord_is_finite(
            all_distances,
            all_x_coords,
            all_y_coords,
            all_distances[distances_index],
            x_coords,
            y_coords,
            distances_index,
        )
        numbers_of_closest_points.append(closest_point)
        finite_coords.extend(finite_coord)
    return numbers_of_closest_points, finite_coords


def zip_coords_with_numbers_of_closest_points(coords, all_numbers_of_closest_points):
    coords_and_number_of_points = []
    for idx, coords in enumerate(coords):
        coords_and_number_of_points.append([coords, all_numbers_of_closest_points[idx]])
    return coords_and_number_of_points


def get_max_finite_coords_numbers_of_closest_points(
    zipped_coords_with_numbers_of_closest_points, finite_coords
):
    finite_coords_numbers_of_closest_points = []
    for (
        coords,
        numbers_of_closest_points,
    ) in zipped_coords_with_numbers_of_closest_points:
        if coords in finite_coords:
            finite_coords_numbers_of_closest_points.append(numbers_of_closest_points)
    return max(finite_coords_numbers_of_closest_points)


if __name__ == "__main__":

    x_coords, y_coords = get_input_coords(inputs)
    all_distances, all_x_coords, all_y_coords = get_distance_to_all_points(
        x_coords, y_coords
    )
    all_numbers_of_closest_points, finite_coords = get_all_numbers_of_closest_points(
        all_distances, x_coords, y_coords, all_x_coords, all_y_coords
    )
    zipped_coords_with_numbers_of_closest_points = zip_coords_with_numbers_of_closest_points(
        zip(x_coords, y_coords), all_numbers_of_closest_points
    )
    print(
        get_max_finite_coords_numbers_of_closest_points(
            zipped_coords_with_numbers_of_closest_points, finite_coords
        )
    )
