with open("input1_2019.txt", "r") as f:
    mass_list = f.read().split("\n")


def calculate_sum_of_fuel_part1(list_of_mass):
    sum_of_fuel = 0
    for mass in list_of_mass:
        fuel = int((int(mass) / 3) - 2)
        sum_of_fuel += fuel
    return sum_of_fuel


def calculate_sum_of_fuel_part_2(mass_list):
    final_sum_of_fuel = 0
    for mass in mass_list:
        fuel = int((int(mass) / 3) - 2)
        while fuel > 0:
            final_sum_of_fuel += fuel
            fuel = int((int(fuel) / 3) - 2)
    return final_sum_of_fuel

if __name__ == "__main__":

    print(f" first answer: {calculate_sum_of_fuel_part1(mass_list)}")
    print(f" second answer: {calculate_sum_of_fuel_part_2(mass_list)}")
