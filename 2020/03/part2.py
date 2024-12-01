import math

trees = []
cursor = 0
increments = [1, 3, 5, 7, 1]

with open("input.txt") as f:
    lines = list(filter(None, f.read().split("\n")))

    for index, increment in enumerate(increments):
        if index == len(increments) - 1:
            print("last go around!")
            lines = lines[::2]

        cursor = 0
        tree_count = 0

        for line in lines:

            # Wrapping around a 2D array https://stackoverflow.com/a/9058387
            if cursor < 0:
                cursor += len(line)
            elif cursor >= len(line):
                cursor = cursor % len(line)

            if line[cursor] == "#":
                tree_count += 1

            cursor += increment

        trees.append(tree_count)

print(trees)
print(math.prod(trees))
