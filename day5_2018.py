input5 = [open("input5.txt").read()]


def get_separate_letters(inputs):
    new_inputs = []
    for line in inputs:
        for letter in line:
            new_inputs.append(letter)
    return new_inputs


def pop_letters_from_inputs(inputs, letter_idx):
    inputs.pop(letter_idx)
    inputs.pop(letter_idx)


def get_all_possible_reactions(inputs):
    for letter_idx, first_letter in enumerate(inputs):
        if letter_idx == len(inputs) - 1:
            break
        for second_letter in inputs[letter_idx + 1]:
            if first_letter.isupper():
                if second_letter == first_letter.lower():
                    pop_letters_from_inputs(inputs, letter_idx)
            if first_letter.islower():
                if second_letter == first_letter.upper():
                    pop_letters_from_inputs(inputs, letter_idx)
    return len(inputs)


def get_answer(inputs):
    result = False
    num_of_letters = []
    while result is False:
        reactions = get_all_possible_reactions(inputs)
        if reactions in num_of_letters:
            result = True
        num_of_letters.append(reactions)
    return num_of_letters[-1]


def get_specific_letters(inputs):
    specific_letters = set(inputs)
    letters_to_find = []
    for letter in specific_letters:
        if letter.lower() in letters_to_find or letter.upper() in letters_to_find:
            continue
        else:
            letters_to_find.append(letter)
    return letters_to_find


def get_inputs_without_letter(inputs, idx_of_deleted_letter):
    for letter_idx, first_letter in enumerate(inputs[idx_of_deleted_letter]):
        for compare_letter in inputs[(letter_idx + 1) :]:
            if (
                first_letter.upper() == compare_letter
                or first_letter.lower() == compare_letter
            ):
                inputs.pop(inputs.index(compare_letter))
    return inputs

def get_answer_part_2(inputs):
    letters_to_find = get_specific_letters(inputs)
    num_of_reactions = []
    for letter_to_find_idx in range(len(letters_to_find)):
        inputs = get_separate_letters(input5)
        index = inputs.index(letters_to_find[letter_to_find_idx])
        input_part_2 = get_inputs_without_letter(inputs, index)
        num_of_reactions.append(get_answer(input_part_2))
    return min(num_of_reactions)


if __name__ == "__main__":

    inputs = get_separate_letters(input5)
    print(f"Answer for part 1: {get_answer(inputs)}")

    print(f"Answer for part 2: {get_answer_part_2(inputs)}")
