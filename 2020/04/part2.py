import re

valid = 0
# For generating the numeric range regexes: http://gamon.webfactional.com/regexnumericrangegenerator/

fields = {
    "byr": r"byr:(19[2-8][0-9]|199[0-9]|200[0-2])\b",
    "iyr": r"iyr:(201[0-9]|2020)\b",
    "eyr": r"eyr:(202[0-9]|2030)\b",
    "hgt": r"hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6]))in)\b",
    "hcl": r"hcl:#([a-f|0-9]{6})\b",
    "ecl": r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b",
    "pid": r"pid:([0-9]{9})\b",
}


with open("input.txt") as f:
    lines = list(filter(None, f.read().split("\n\n")))

    for line in lines:
        line = line.replace("\n", " ").rstrip()
        matches = []
        for field, validation_regex in fields.items():
            matches.append(re.search(validation_regex, line))
        if all(matches):
            valid += 1
print(valid)
