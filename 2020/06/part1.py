# Decided to make Day 6 my first foray into code golf. I can reduce it
# further but want to move on to Day 7
count = 0

with open("input.txt") as f:
    for line in list(filter(None, f.read().split("\n\n"))):
        count += len(set.intersection(*list(map(lambda x: set(x), list(map(lambda x: set(x), list(map(lambda x: set(x), line.split("\n"))),)),))))

print(count)
