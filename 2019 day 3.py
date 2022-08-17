first_cable, second_cable = open("input3_2019.txt").read().split("\n")
first_cable, second_cable = [x.split(",") for x in [first_cable, second_cable]]


def cables_intersection(cable_coords):
    cable_xy = []
    xy = [0, 0]
    for movement in cable_coords:
        for i in range(int(movement[1:])):
            cable_xy.append(tuple(xy[:]))
            if movement[0] == "U":
                xy[1] += 1
            elif movement[0] == "D":
                xy[1] -= 1
            elif movement[0] == "L":
                xy[0] -= 1
            elif movement[0] == "R":
                xy[0] += 1
    return cable_xy


if __name__ == "__main__":

    first_cable_coords = cables_intersection(first_cable)
    second_cable_coords = cables_intersection(second_cable)
    results = list(set(first_cable_coords).intersection(set(second_cable_coords)))
    final_result = min(sum(i) for i in results if sum(i) > 0)
    steps = []
    for result in results:
        first_cable_steps = first_cable_coords.index(result)
        seconds_cable_steps = second_cable_coords.index(result)
        sum_of_steps = first_cable_steps + seconds_cable_steps
        if sum_of_steps > 0:
            steps.append(sum_of_steps)
    final_steps = min(steps)
    print(f"The answer to part 1 is: {final_result}")
    print(f"The answer to part 2 is: {final_steps}")

    ## old, slower code:
    # def calc_steps(idx, cable_coords):
    #     steps = 0
    #     cable_xy = []
    #     xy = [0, 0]
    #     number_of_steps = []
    #     for movement in cable_coords:
    #         for move in range(int(movement[1:])):
    #             cable_xy.append(tuple(xy[:]))
    #             if movement[0] == "U":
    #                 xy[1] += 1
    #             elif movement[0] == "D":
    #                 xy[1] -= 1
    #             elif movement[0] == "L":
    #                 xy[0] -= 1
    #             elif movement[0] == "R":
    #                 xy[0] += 1
    #             if results[idx] in cable_xy:
    #                 number_of_steps.append(steps)
    #                 break
    #             steps += 1
    #     set_number_of_steps = set(number_of_steps)
    #     list_number_of_steps = list(set_number_of_steps)
    #     return list_number_of_steps

    # first_cable_steps = []
    # second_cable_steps = []
    # final_steps = []
    # for result_index in range(len(results)):
    #     first_cable_steps.append(calc_steps(result_index, first_cable))
    #     second_cable_steps.append(calc_steps(result_index, second_cable))
    # sum_of_final_steps = [
    #     first_cable_steps[i] + second_cable_steps[i]
    #     for i in range(len(first_cable_steps))
    # ]
    # for res in sum_of_final_steps:
    #     final_steps.append(res[1] + res[0])
    # final_steps = min(x for x in final_steps if x > 0)
