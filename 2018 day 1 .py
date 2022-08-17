with open("input1_2018.txt", "r") as f:
    input = f.read().split("\n")


def do_first_exercise(input):
    changes_of_frequency = []
    frequency = 0
    for frequency_change in input:
        amount = int(frequency_change[1:])
        if frequency_change[0] == "+":
            frequency += amount
        else:
            frequency -= amount
        changes_of_frequency.append(frequency)
    return frequency


def do_second_exercise(input):
    frequency = 0
    changes_of_frequency = {frequency}
    found = 0
    answer = ""
    while found == 0:
        for frequency_change in input:
            amount = int(frequency_change[1:])
            if frequency_change[0] == "+":
                frequency += amount
            else:
                frequency -= amount
            if frequency in changes_of_frequency:
                answer = frequency
                found = 1
                break
            changes_of_frequency.add(frequency)
    return answer


if __name__ == "__main__":

    print(f"first answer: {do_first_exercise(input)}, second answer: {do_second_exercise(input)}")
