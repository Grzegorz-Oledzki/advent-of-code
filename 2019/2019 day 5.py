def do_first_exercise(integers):
    for idx, integer in enumerate(integers):

        if integer == 1:
            integers[integers[idx + 3]] = (
                integers[integers[idx + 1]] + integers[integers[idx + 2]]
            )

        elif integer == 2:
            integers[integers[idx + 3]] = (
                integers[integers[idx + 1]] * integers[integers[idx + 2]]
            )

        elif integer == 3:
            integers[integers[idx + 1]] = int(input("1 or 5?"))

        elif integer == 4:
            result = integers[integers[idx + 1]]
            integers[integers[idx + 1]] = result

        elif integer == 99:
            break
    return integers[0]


def generate_second_exercise_answer(noun, verb):
    return 100 * noun + verb


if __name__ == "__main__":
    list_of_integers = [
        int(x) for x in open("input5_2019.txt").read().split(",")
    ]
    print(list_of_integers)
    print(do_first_exercise(list_of_integers))