from collections import defaultdict, Counter

f = open("12.txt", "r")
f2 = open("12mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

def isValid(n, path, allow_revisit):
    return n != "start" and (n == "end" or n.isupper() or n not in path or (max(Counter([i for i in path if i.islower()]).values()) == 1 and allow_revisit)) 

def traverse(inputs, allow_revisit = False):
    neighbors = defaultdict(set)
    for i in inputs:
        t, f = i.split("-")
        neighbors[t].add(f)
        neighbors[f].add(t)
    total = 0
    queue = [("start", ["start"])]
    while queue:
        curr, path = queue.pop()
        if curr == "end":
            total += 1
            continue
        for n in neighbors[curr]:
            if isValid(n, path, allow_revisit):
                queue.append((n, path + [n]))
    return total

#Part 1
def part1(inputs):
    return traverse(inputs, False)

#Part 2
def part2(inputs):
    return traverse(inputs, True)

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))