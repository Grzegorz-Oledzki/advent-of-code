with open("input6_2018.txt", "r") as file:
    inputs = file.read().split("\n")
from collections import namedtuple

inputs = [x.split(", ") for x in inputs]
Point = namedtuple("Point", ["x", "y"])


def get_coords_from_input(inputs):
    x_coords = [int(coord[0]) for coord in inputs]
    y_coords = [int(coord[1]) for coord in inputs]
    return x_coords, y_coords


def get_points_for_manhattan_distance(row_idx, column_idx, x_coord, y_coord):
    return Point(x=x_coord, y=y_coord), Point(x=row_idx, y=column_idx)


def manhattan_distance(first_and_second_points):
    first_point, second_point = first_and_second_points[0], first_and_second_points[1]
    return abs(first_point.x - second_point.x) + abs(first_point.y - second_point.y)


def coords_extremes(x_coords, y_coords):
    return min(x_coords), max(x_coords), min(y_coords), max(y_coords)


def get_distance_to_all_points(x_coords, y_coords):
    all_distances, all_x_coords, all_y_coords = [], [], []
    for x_coord, y_coord in zip(x_coords, y_coords):
        distance = []
        for row_idx in range(max(x_coords)):
            for column_idx in range(max(y_coords)):
                distance.append(
                    manhattan_distance(
                        get_points_for_manhattan_distance(
                            row_idx, column_idx, x_coord, y_coord
                        )
                    )
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
    min_x, max_x, min_y, max_y = coords_extremes(x_coords, y_coords)
    closest_points = 0
    finest_point = []
    x_coords_of_the_nearest_points, y_coords_of_the_nearest_points = [], []
    for distance_idx, distance in enumerate(distances):
        count = 0
        for second_distance in all_distances:
            if distance < second_distance[distance_idx]:
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
    for distances_index, distance in enumerate(all_distances):
        (
            closest_point,
            finite_coord,
        ) = get_number_of_closest_points_and_check_if_coord_is_finite(
            all_distances,
            all_x_coords,
            all_y_coords,
            distance,
            x_coords,
            y_coords,
            distances_index,
        )
        numbers_of_closest_points.append(closest_point)
        finite_coords.extend(finite_coord)
    return numbers_of_closest_points, finite_coords


def zip_coords_with_numbers_of_closest_points(
    coords_to_zip, all_numbers_of_closest_points
):
    coords_and_number_of_points = []
    for idx, coords in enumerate(coords_to_zip):
        coords_and_number_of_points.append([coords, all_numbers_of_closest_points[idx]])
    return coords_and_number_of_points


def get_max_finite_coords_numbers_of_closest_points(
    zipped_coords_with_numbers_of_closest_points, finite_coords
):
    finite_coords_numbers_of_closest_points = [
        numbers_of_closest_points
        for coords, numbers_of_closest_points in zipped_coords_with_numbers_of_closest_points
        if coords in finite_coords
    ]
    return max(finite_coords_numbers_of_closest_points)


def get_answer_for_part_1(inputs):
    x_coords, y_coords = get_coords_from_input(inputs)
    all_distances, all_x_coords, all_y_coords = get_distance_to_all_points(
        x_coords, y_coords
    )
    all_numbers_of_closest_points, finite_coords = get_all_numbers_of_closest_points(
        all_distances, x_coords, y_coords, all_x_coords, all_y_coords
    )
    return f"Part 1: {get_max_finite_coords_numbers_of_closest_points(zip_coords_with_numbers_of_closest_points(zip(x_coords, y_coords), all_numbers_of_closest_points), finite_coords)} "


def get_distance_to_all_coords(x_coords, y_coords):
    all_distances = []
    for row_idx in range(max(x_coords)):
        for column_idx in range(max(y_coords)):
            distances = [
                manhattan_distance(
                    get_points_for_manhattan_distance(
                        row_idx, column_idx, x_coord, y_coord
                    )
                )
                for x_coord, y_coord in zip(x_coords, y_coords)
            ]
            sum_of_distances = sum(distances)
            if sum_of_distances < 10000:
                all_distances.append(sum_of_distances)
    return len(all_distances)


def get_answer_to_part_2(inputs):
    x_coords, y_coords = get_coords_from_input(inputs)
    return f"Part 2: {get_distance_to_all_coords(x_coords,y_coords)}"


if __name__ == "__main__":

    print(get_answer_for_part_1(inputs))
    print(get_answer_to_part_2(inputs))
