import re

valid = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("input.txt") as f:
    lines = f.read().split("\n\n")

    for line in lines:
        line = line.replace("\n", " ")

        matches = []
        for field in fields:
            matches.append(re.search(rf"{field}:([#a-zA-Z0-9]+)", line))

        if all(matches):
            valid += 1

print(valid)
