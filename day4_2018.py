with open("input4.txt", "r") as f:
    inputs = f.read().split("\n")
    inputs.sort()
    inputs = [x.split(" ") for x in inputs]


def get_guards_ids(inputs):
    guards_id = []
    for data_line in inputs:
        if len(data_line) == 6 and data_line[3][1:] not in guards_id:
            guards_id.append(data_line[3][1:])
    return guards_id


def get_length_of_next_asleep(idx):
    guard_asleep_minutes = 0
    specific_asleep_minutes = []
    if idx < len(inputs) - 3:
        wake_up = inputs[idx + 4][1]
        asslep = inputs[idx + 3][1]
        if inputs[idx + 3][3] == "asleep":
            length_of_sleep = int(wake_up[3:5]) - int(asslep[3:5])
            guard_asleep_minutes += length_of_sleep
            for minutes in range(int(asslep[3:5]), int(wake_up[3:5])):
                specific_asleep_minutes.append(minutes)
    return guard_asleep_minutes, specific_asleep_minutes


def get_guard_asleep_minutes(inputs, guard_ids_index):
    guard_asleep_minutes = []
    specific_asleep_minutes = []
    for idx, data_line in enumerate(inputs):
        if (
            data_line[3][1:] == gurads_ids[guard_ids_index]
            and inputs[idx + 1][3] == "asleep"
        ):
            wake_up = inputs[idx + 2][1]
            asslep = inputs[idx + 1][1]
            length_of_sleep = int(wake_up[3:5]) - int(asslep[3:5])
            guard_asleep_minutes.append(length_of_sleep)
            for minutes in range(int(asslep[3:5]), int(wake_up[3:5])):
                specific_asleep_minutes.append(minutes)
            if get_length_of_next_asleep(idx)[0] > 0:
                guard_asleep_minutes.append(get_length_of_next_asleep(idx)[0])
                guard_asleep_minutes.append(get_length_of_next_asleep(idx + 1)[0])  #
                specific_asleep_minutes.extend(get_length_of_next_asleep(idx)[1])
    return guard_asleep_minutes, specific_asleep_minutes


def most_frequent(List):
    counter = 0
    num = List
    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num


def get_answer_to_part1(guards_ids):
    sums_of_guards_asleep = []
    for guards_idx in range(len(gurads_ids)):
        guard = get_guard_asleep_minutes(inputs, guards_idx)
        sums_of_guards_asleep.append(sum(guard[0]))
    most_asleep_guard_idx = sums_of_guards_asleep.index(max((sums_of_guards_asleep)))
    minute_when_he_sleeps = most_frequent(
        get_guard_asleep_minutes(inputs, most_asleep_guard_idx)[1]
    )
    return f"Part 1: {int(gurads_ids[most_asleep_guard_idx]) * minute_when_he_sleeps}"


def get_answer_to_part2(guards_ids):
    num_of_guard_most_asleep_minute = []
    for guards_idx in range(len(gurads_ids)):
        guard = get_guard_asleep_minutes(inputs, guards_idx)
        num_of_guard_most_asleep_minute.append(guard[1].count(most_frequent(guard[1])))
    most_one_minute_asleep_guard_idx = num_of_guard_most_asleep_minute.index(
        max(num_of_guard_most_asleep_minute)
    )
    minute_when_he_sleeps = most_frequent(
        get_guard_asleep_minutes(inputs, most_one_minute_asleep_guard_idx)[1]
    )
    return f"Part 2: {int(gurads_ids[most_one_minute_asleep_guard_idx]) * minute_when_he_sleeps}"


if __name__ == "__main__":

    gurads_ids = get_guards_ids(inputs)
    # part 1
    print(get_answer_to_part1(gurads_ids))

    # part 2
    print(get_answer_to_part2(gurads_ids))
