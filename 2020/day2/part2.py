import re

valid = 0
input_parser = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")

with open("input.txt") as f:
    for line in list(filter(None, f.read().split("\n"))):
        minimum, maximum, character, password = input_parser.match(line).groups()

        min_char = password[int(minimum) - 1]
        max_char = password[int(maximum) - 1]

        if (min_char == character) ^ (max_char == character):
            valid += 1

print(valid)
