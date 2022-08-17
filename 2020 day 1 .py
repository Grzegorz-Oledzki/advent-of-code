with open("input1_2020.txt", "r") as f:
    file = f.read().splitlines()
first_answer = ""
second_answer = ""

for first_number in file:
    first_number = int(first_number)
    for second_number in file:
        second_number = int(second_number)
        sum_of_numbers = first_number + second_number
        if sum_of_numbers == 2020:
            first_answer = first_number * second_number
        for third_number in file:
            third_number = int(third_number)
            sum_of_numbers = first_number + second_number + third_number
            if sum_of_numbers == 2020:
                second_answer = first_number * second_number * third_number

print(f"first answer: {first_answer}, second answer: {second_answer}")
