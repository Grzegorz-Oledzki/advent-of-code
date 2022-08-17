with open("input2_2020.txt", "r") as f:
    file = f.read().splitlines()
count = 0
a = 0
for txtfile in file:
    txtfilesplitted = txtfile.split(" ")
    number_of_appearances = txtfilesplitted[0]
    numbers = number_of_appearances.split("-")
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    letter_to_find = txtfilesplitted[1]
    text = txtfilesplitted[2]
    number3 = number1 - 1
    number4 = number2 - 1
    count += 1

    if text[number3] == letter_to_find[0] or text[number4] == letter_to_find[0]:
        a = a + 1
        if text[number3] == letter_to_find[0] and text[number4] == letter_to_find[0]:
            a = a - 1
print(f"second answer: {a}")
