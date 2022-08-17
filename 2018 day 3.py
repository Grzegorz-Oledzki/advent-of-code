import numpy as np

with open("input3_2018.txt", "r") as f:
    inputs = f.read().split("\n")
    inputs = [x.split(" ") for x in inputs]


def get_starting_points_and_dimensions(data):
    start_points = []
    dimensions = []
    for code in data:
        pre_starting_point = code[2][:-1]
        pre_dimension = code[3]
        pre_starting_point = pre_starting_point.split(",")
        pre_dimension = pre_dimension.split("x")
        start_points.append((int(pre_starting_point[0]), int(pre_starting_point[1])))
        dimensions.append((int(pre_dimension[0]), int(pre_dimension[1])))
    return start_points, dimensions


def get_sum_of_claims_squares(area):
    sum_of_squares_within_two_or_more_claims = 0
    for row_idx in range(1000):
        for column_idx in range(1000):
            if area[row_idx, column_idx] > 1:
                sum_of_squares_within_two_or_more_claims += 1
    return sum_of_squares_within_two_or_more_claims


if __name__ == "__main__":
    area = np.zeros((1000, 1000))
    data = get_starting_points_and_dimensions(inputs)

    for starting_point, dimension in zip(data[0], data[1]):
        area[
            starting_point[0]: starting_point[0] + dimension[0],
            starting_point[1]: starting_point[1] + dimension[1],
        ] += 1
    print(f"first answer: {get_sum_of_claims_squares(area)}")

    idx = 1
    for starting_point, dimension in zip(data[0], data[1]):
        part_of_the_arena = area[
            starting_point[0] : starting_point[0] + dimension[0],
            starting_point[1] : starting_point[1] + dimension[1],
        ]
        sum_of_claim_in_squares = 0
        if sum(sum(part_of_the_arena)) == part_of_the_arena.size:
            print(f"second answer:{idx}")
        idx += 1
