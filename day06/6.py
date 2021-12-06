from collections import defaultdict

f = open("6.txt", "r")
f2 = open("6mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

#Part 1
def part1(inputs):
    inputs = [int(i) for i in inputs[0].split(",")]
    zeroes = 0
    length = len(inputs)
    for num in range(80):
        newinputs = []
        for i in inputs:
            if i == 0:
                newinputs.append(8)
                newinputs.append(6)
            else:
                newinputs.append(i-1)
        inputs = newinputs
    return len(inputs)
    
#Part 2
def part2(inputs):
    inputs = [int(i) for i in inputs[0].split(",")]
    counts = defaultdict(int)
    for i in set(inputs):
        counts[i] = inputs.count(i)
    for num in range(256):
        newcounts = defaultdict(int)
        for i in counts:
            ct = counts[i]
            if i == 0:
                newcounts[8] += ct
                newcounts[6] += ct
            else:
                newcounts[i-1] += ct
        counts = newcounts
    return sum(counts.values())

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))