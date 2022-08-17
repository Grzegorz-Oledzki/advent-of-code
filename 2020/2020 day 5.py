with open("input5_2020.txt") as f:
    passport_list = f.read().splitlines()


def get_half_of_the_list(list_of_seats, letter):
    half_of_seats = int(len(list_of_seats) / 2)
    if letter in ["F", "L"]:
        return list_of_seats[:half_of_seats]
    else:
        return list_of_seats[half_of_seats:]


def checking_seat_ID(row, column):
    return row * 8 + column


def get_single_value(list_of_seats, letters):
    new_list = list_of_seats
    for letter in letters:
        new_list = get_half_of_the_list(new_list, letter)
    return new_list[0]


if __name__ == "__main__":

    rows = list(range(128))
    columns = list(range(8))
    seat_ids = []
    possible_user_seats = list(range(99, 974))
    for passport in passport_list:
        row_id = get_single_value(rows, passport[:7])
        column_id = get_single_value(columns, passport[7:])

        seat_id = checking_seat_ID(row_id, column_id)
        seat_ids.append(seat_id)
    user_seat = list(set(possible_user_seats) - set(seat_ids))
    print(f"first answer:{max(seat_ids)},second answer: {user_seat}")
