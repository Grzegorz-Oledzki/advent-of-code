with open("input2_2018.txt", "r") as f:
    inputs = f.read().split("\n")


def get_result_of_part_one(inputs):
    num_of_codes_with_two_same_letters = 0
    num_of_codes_with_three_same_letters = 0
    for code in inputs:
        are_there_two_letters = False
        are_there_three_letters = False
        for letter in code:
            if code.count(letter) == 2:
                are_there_two_letters = True
            if code.count(letter) == 3:
                are_there_three_letters = True
        if are_there_two_letters:
            num_of_codes_with_three_same_letters += 1
        if are_there_three_letters:
            num_of_codes_with_two_same_letters += 1
    return num_of_codes_with_three_same_letters * num_of_codes_with_two_same_letters


def get_result_of_part_two(inputs):
    for first_code_idx, first_code in enumerate(inputs):
        for second_code in inputs[(first_code_idx + 1) :]:
            for letter_idx, letter in enumerate(second_code):
                if (
                    second_code[:letter_idx] == first_code[:letter_idx]
                    and second_code[letter_idx + 1 :] == first_code[letter_idx + 1 :]
                ):
                    return first_code[:letter_idx] + first_code[letter_idx + 1 :]


if __name__ == "__main__":
    print(f"part 1: {get_result_of_part_one(inputs)}")
    print(f"part 1: {get_result_of_part_two(inputs)}")
