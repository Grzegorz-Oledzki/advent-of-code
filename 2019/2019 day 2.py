def do_first_exercise(integers):
    for idx, integer in enumerate(integers):
        if idx % 4 == 0:
            if integer == 1:
                result = integers[integers[idx + 1]] + integers[integers[idx + 2]]
                integers[integers[idx + 3]] = result

            elif integer == 2:
                result = integers[integers[idx + 1]] * integers[integers[idx + 2]]
                integers[integers[idx + 3]] = result

            elif integer == 99:
                break
    return integers[0]


def generate_second_exercise_answer(noun, verb):
    return 100 * noun + verb


if __name__ == "__main__":

    expected_output = 19690720
    for noun in range(100):
        for verb in range(100):
            list_of_integers = [
                int(x) for x in open("input2_2019.txt").read().split(",")
            ]
            list_of_integers[1] = noun
            list_of_integers[2] = verb
            result = do_first_exercise(list_of_integers)
            if result == expected_output:
                print(f"second answer: {generate_second_exercise_answer(noun, verb)}")
