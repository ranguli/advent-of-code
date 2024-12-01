trees = 0
cursor = 0
increment = 3

with open("input.txt") as f:
    lines = list(filter(None, f.read().split("\n")))
    for line in lines:
        # Wrapping around a 2D array https://stackoverflow.com/a/9058387
        if cursor < 0:
            cursor += len(line)
        elif cursor >= len(line):
            cursor = cursor % len(line)

        if line[cursor] == "#":
            trees += 1

        cursor += increment
print(trees)
