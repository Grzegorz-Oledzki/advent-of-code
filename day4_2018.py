with open("input4.txt", "r") as f:
    inputs = f.read().split("\n")

inputs.sort()
inputs = [x.split(" ") for x in inputs]


def get_guards_ids(inputs):
    return list(set([data_line[3][1:] for data_line in inputs if len(data_line) == 6]))


def get_guard_next_asleep_time_and_specific_minutes(idx, guards_input):
    guard_asleep_minutes = 0
    specific_asleep_minutes = []
    if idx < len(guards_input) - 3:
        wake_up = int(inputs[idx + 4][1][3:5])
        asleep = int(inputs[idx + 3][1][3:5])
        if inputs[idx + 3][3] == "asleep":
            specific_asleep_minutes = list(range(asleep, wake_up))
            guard_asleep_minutes = len(specific_asleep_minutes)
    return guard_asleep_minutes, specific_asleep_minutes


def get_guard_asleep_time_and_specific_minutes(guards_input, guard_id):
    guard_asleep_minutes = []
    specific_asleep_minutes = []
    for idx, data_line in enumerate(guards_input):
        data_line_guard_id = data_line[3][1:]
        if data_line_guard_id == guard_id and guards_input[idx + 1][3] == "asleep":
            wake_up = int(guards_input[idx + 2][1][3:5])
            asleep = int(guards_input[idx + 1][1][3:5])
            length_of_sleep = wake_up - asleep
            guard_asleep_minutes.append(length_of_sleep)
            specific_asleep_minutes.extend(
                list(range(asleep, wake_up))
            )
            guard_next_asleep_time, guard_asleep_specific_minutes = get_guard_next_asleep_time_and_specific_minutes(
                idx, guards_input
            )
            if guard_next_asleep_time > 0:
                guard_asleep_minutes.append(guard_next_asleep_time)
                specific_asleep_minutes.extend(guard_asleep_specific_minutes)
    return guard_asleep_minutes, specific_asleep_minutes


def most_frequent(guard_minutes):
    dict = {}
    count, itm = 0, ""
    for item in reversed(guard_minutes):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return itm


def get_answer_to_part1(guards_ids, guards_input):
    most_sleeping_time = 0
    guard_who_slept_most_time_id = None
    for guard_id in guards_ids:
        guard_asleep_minutes = get_guard_asleep_time_and_specific_minutes(
            guards_input, guard_id
        )[0]
        if sum(guard_asleep_minutes) > most_sleeping_time:
            most_sleeping_time = sum(guard_asleep_minutes)
            guard_who_slept_most_time_id = guard_id
    minute_when_he_sleeps = most_frequent(
        get_guard_asleep_time_and_specific_minutes(
            guards_input, guard_who_slept_most_time_id
        )[1]
    )
    return f"Part 1: {int(guard_who_slept_most_time_id) * minute_when_he_sleeps}"


def get_answer_to_part2(guards_ids):
    num_of_guard_most_asleep_minute = []
    guard_minute_asleep = []
    for guard_id in guards_ids:
        guard_asleep_time_and_minutes = get_guard_asleep_time_and_specific_minutes(
            inputs, guard_id
        )
        guard_minute_asleep.append(guard_asleep_time_and_minutes)
        num_of_guard_most_asleep_minute.append(
            guard_asleep_time_and_minutes[1].count(
                most_frequent(guard_asleep_time_and_minutes[1])
            )
        )
    most_one_minute_asleep_guard_idx = num_of_guard_most_asleep_minute.index(
        max(num_of_guard_most_asleep_minute)
    )
    minute_when_he_sleeps = most_frequent(
        get_guard_asleep_time_and_specific_minutes(
            inputs, guards_ids[most_one_minute_asleep_guard_idx]
        )[1]
    )
    return f"Part 2: {int(guards_ids[most_one_minute_asleep_guard_idx]) * minute_when_he_sleeps}"


if __name__ == "__main__":

    guards_ids = get_guards_ids(inputs)
    # part 1
    print(get_answer_to_part1(guards_ids, inputs))

    # part 2
    print(get_answer_to_part2(guards_ids))
