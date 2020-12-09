import math

valid = 0


line = "FBFBBFFRLR"


def process_row(line):
    min_range = 0
    max_range = 127
    line = line[:7]

    for character in line:
        if character == "F":
            max_range = (min_range + max_range) // 2
        elif character == "B":
            min_range = math.ceil((min_range + max_range) / 2)

    return min_range


def process_column(line):
    min_range = 0
    max_range = 8
    line = line[7:]

    for character in line:
        if character == "L":
            max_range = (min_range + max_range) // 2
        elif character == "R":
            min_range = math.ceil((min_range + max_range) / 2)

    return min_range


with open("input.txt") as f:
    highest_seat_id = 0
    lines = f.read().split("\n")

    for line in lines:
        row = process_row(line)
        column = process_column(line)
        seat_id = row * 8 + column

        print(f"{line} - {row} - {column} - {seat_id}")

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print(highest_seat_id)
