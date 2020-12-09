import math


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


def process_aisle(line):
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
    seats = {}
    highest_seat_id = 0
    lines = list(filter(None, f.read().split("\n")))

    for line in lines:
        row = process_row(line)
        aisle = process_aisle(line)
        seat_id = row * 8 + aisle

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

        if seats.get(row):
            seats[row].append(aisle)
        else:
            seats[row] = [aisle]

    lowest = sorted(seats.keys())[0]
    highest = sorted(seats.keys())[-1]

    del seats[lowest]
    del seats[highest]

    normal_aisle = [i for i in range(8)]

    for row, aisle in seats.items():
        aisle.sort()
        if len(aisle) != 8:
            aisle_number = list(set(normal_aisle) - set(aisle))[0]
            print(row * 8 + aisle_number)
            break
