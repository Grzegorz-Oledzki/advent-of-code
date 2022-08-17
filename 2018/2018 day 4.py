with open("input4_2018.txt", "r") as f:
    inputs = f.read().split("\n")

inputs.sort()
inputs = [x.split(" ") for x in inputs]


def get_guards_ids(inputs):
    return list(set([data_line[3][1:] for data_line in inputs if len(data_line) == 6]))


def get_guard_next_asleep_time_and_specific_minutes(idx, guards_input):
    if idx < len(guards_input) - 3:
        wake_up, asleep = get_next_wake_up_and_asleep_time(idx, guards_input)
        specific_asleep_minutes, guard_asleep_minutes = get_specific_asleep_and_guard_asleep_minutes(
            wake_up, asleep, idx
        )
        return guard_asleep_minutes, specific_asleep_minutes
    return (
        None,
        None,
    )


def get_next_wake_up_and_asleep_time(idx, guards_input):
    return int(guards_input[idx + 4][1][3:5]), int(guards_input[idx + 3][1][3:5])


def get_specific_asleep_and_guard_asleep_minutes(wake_up, asleep, idx):
    if inputs[idx + 3][3] == "asleep":
        return list(range(asleep, wake_up)), len(range(asleep, wake_up))
    return None, None


def get_guard_asleep_time_and_specific_minutes(guards_input, guard_id):
    guard_asleep_minutes = []
    specific_asleep_minutes = []
    for idx, data_line in enumerate(guards_input):
        if finding_right_guard_line(data_line, guard_id, guards_input, idx):
            wake_up, asleep, length_of_sleep = get_wake_up_and_asleep_time(
                guards_input, idx
            )
            guard_asleep_minutes.append(length_of_sleep)
            specific_asleep_minutes.extend(list(range(asleep, wake_up)))
            guard_next_asleep_time, guard_asleep_specific_minutes = get_guard_next_asleep_time_and_specific_minutes(
                idx, guards_input
            )
            append_and_extend_guard_asleep_minutes(
                guard_asleep_minutes,
                specific_asleep_minutes,
                guard_next_asleep_time,
                guard_asleep_specific_minutes,
            )
    return sum(guard_asleep_minutes), specific_asleep_minutes


def finding_right_guard_line(data_line, guard_id, guards_input, idx):
    data_line_guard_id = data_line[3][1:]
    if data_line_guard_id == guard_id and guards_input[idx + 1][3] == "asleep":
        return True


def get_wake_up_and_asleep_time(guards_input, idx):
    return (
        int(guards_input[idx + 2][1][3:5]),
        int(guards_input[idx + 1][1][3:5]),
        int(guards_input[idx + 2][1][3:5]) - int(guards_input[idx + 1][1][3:5]),
    )


def append_and_extend_guard_asleep_minutes(
    guard_asleep_minutes,
    specific_asleep_minutes,
    guard_next_asleep_time,
    guard_asleep_specific_minutes,
):
    if guard_next_asleep_time:
        return (
            guard_asleep_minutes.append(guard_next_asleep_time),
            specific_asleep_minutes.extend(guard_asleep_specific_minutes),
        )


def most_frequent(sleep_minutes):
    dict = {}
    count, itm = 0, ""
    for item in reversed(sleep_minutes):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return itm


def get_answer_to_part1(guards_ids, guards_input):
    most_sleeping_time, minute_when_he_sleeps = 0, 0
    guard_who_slept_most_time_id = None
    for guard_id in guards_ids:
        guard_asleep_minutes, sleep_minutes = get_guard_asleep_time_and_specific_minutes(
            guards_input, guard_id
        )
        if guard_asleep_minutes > most_sleeping_time:
            guard_who_slept_most_time_id, minute_when_he_sleeps, most_sleeping_time = (
                guard_id,
                most_frequent(sleep_minutes),
                guard_asleep_minutes,
            )
    return f"Part 1: {int(guard_who_slept_most_time_id) * minute_when_he_sleeps}"


def get_answer_to_part2(guards_ids):
    num_of_guard_most_asleep_minute = []
    guard_minute_asleep = []
    for guard_id in guards_ids:
        guard_asleep_time_and_minutes, sleep_minutes = get_guard_asleep_time_and_specific_minutes(
            inputs, guard_id
        )
        guard_minute_asleep.append(guard_asleep_time_and_minutes)
        num_of_guard_most_asleep_minute.append(
            sleep_minutes.count(most_frequent(sleep_minutes))
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