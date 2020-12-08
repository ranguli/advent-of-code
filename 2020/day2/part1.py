import re

input_parser = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
valid = 0

with open("input.txt") as f:
    for line in list(filter(None, f.read().split("\n"))):
        minimum, maximum, character, password = input_parser.match(line).groups()
        occurences = len(re.findall(rf"{character}", password))

        if int(minimum) <= occurences <= int(maximum):
            valid += 1

print(valid)
