# I also accidentally overwrite my part 1 with this after I submitted it :)
# In exchange I made this my first foray into gode colf. It could be reduced
# further but I want to move on to Day 7

count = 0

with open("input.txt") as f:
    for line in list(filter(None, f.read().split("\n\n"))):
        count += len(set.intersection(*list(map(lambda x: set(x), list(map(lambda x: set(x), list(map(lambda x: set(x), line.split("\n"))),)),))))

print(count)
