with open("input3_2020.txt", "r") as f:
    file = f.read().splitlines()


def calculate_num_of_trees(step_right, step_down):
    num_of_trees = 0
    for row_idx, row in enumerate(file):
        movement = step_right * (row_idx // step_down)
        if row[movement % len(row)] == "#" and row_idx % step_down == 0:
            num_of_trees += 1
    return num_of_trees


if __name__ == "__main__":
    steps_right = [1, 3, 5, 7, 1]
    steps_down = [1, 1, 1, 1, 2]

    multiplication_of_trees = 1
    for idx, step_right in enumerate(steps_right):
        num_of_trees = calculate_num_of_trees(step_right, steps_down[idx])
        multiplication_of_trees *= num_of_trees

    print(f" second answer: {multiplication_of_trees}")
