start, end = open("input4_2019.txt").read().split("-")
start, end = [int(x) for x in [start, end]]


def get_two_same_digits(start, end, index):
    numbers_with_two_same_digits = []
    for number in range(start, end):
        number_with_two_same_digits = str(number)
        if number_with_two_same_digits[index] == number_with_two_same_digits[index + 1]:
            numbers_with_two_same_digits.append(number_with_two_same_digits)
    return numbers_with_two_same_digits


def get_numbers_never_decrease(input):
    numbers_never_decrease = []
    for number in input:
        if list(number) == sorted(number):
            numbers_never_decrease.append(number)
    return numbers_never_decrease


def get_pair_numbers(input):
    numbers_with_pair = []
    for number in input:
        for digit in number:
            number_count = number.count(digit)
            if number_count == 2:
                numbers_with_pair.append(number)
    return numbers_with_pair


if __name__ == "__main__":

    final_part1 = []
    for i in range(5):
        input = get_two_same_digits(start, end, i)
        numbers = get_numbers_never_decrease(input)
        final_part1 += numbers

    print(f" Numbers of password in part 1: {len(set(final_part1))}")

    final_part2 = []
    final_numbers = get_pair_numbers(final_part1)
    final_part2 += final_numbers
    print(f" Numbers of password in part 2: {len(set(final_part2))}")
