from collections import defaultdict

f = open("5.txt", "r")
f2 = open("5mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

#Part 1
def part1(inputs):
    counts = defaultdict(int)
    for i in inputs:
        coord1, coord2 = i.split(" -> ")
        x1, y1 = [int(j) for j in coord1.split(",")]
        x2, y2 = [int(j) for j in coord2.split(",")]

        dx = 0 if x1 == x2 else (x2-x1)/abs(x2-x1)
        dy = 0 if y1 == y2 else (y2-y1)/abs(y2-y1)

        x, y = x1, y1
        if dx == 0 or dy == 0:
            while x != x2 or y != y2:
                counts[(x, y)] += 1
                x += dx
                y += dy
            counts[(x, y)] += 1

    return sum(c >= 2 for c in counts.values())
#Part 2
def part2(inputs):
    counts = defaultdict(int)
    for i in inputs:
        coord1, coord2 = i.split(" -> ")
        x1, y1 = [int(j) for j in coord1.split(",")]
        x2, y2 = [int(j) for j in coord2.split(",")]

        dx = 0 if x1 == x2 else (x2-x1)/abs(x2-x1)
        dy = 0 if y1 == y2 else (y2-y1)/abs(y2-y1)

        x, y = x1, y1
        while x != x2 or y != y2:
            counts[(x, y)] += 1
            x += dx
            y += dy
        counts[(x, y)] += 1

    return sum(c >= 2 for c in counts.values())

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))