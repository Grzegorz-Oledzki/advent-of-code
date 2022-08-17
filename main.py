with open("input3_2020.txt", "r") as f:
    file = f.read().splitlines()


for line_idx, line in enumerate(file):
    count = -1
    i1 = 0
    for line in file:
        count += 1
        movementright = 1
        movement = movementright * count
        linelength = len(line)
        line_idx = movement % linelength
        if line_idx % 2 == 0:
            if line[line_idx] == "#":
                i1 += 1
print(i1)
