f = open("11.txt", "r")
f2 = open("11mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

#Part 1
def flash(inputs):
    queue = []
    seen = set()
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            inputs[i][j] += 1
            if inputs[i][j] > 9:
                queue.append((i, j))
                seen.add((i, j))
    while queue:
        j, k = queue.pop()
        for x, y in [(j-1, k-1), (j-1, k), (j-1, k+1), (j, k-1), (j, k+1), (j+1, k-1), (j+1, k), (j+1, k+1)]:
            if 0 <= x < len(inputs) and 0 <= y < len(inputs[0]) and (x, y) not in seen:
                inputs[x][y] += 1
                if inputs[x][y] > 9:
                    seen.add((x, y))
                    queue.append((x, y))
    for x, y in seen:
        inputs[x][y] = 0
    return len(seen)

def part1(inputs):
    inputs = [[int(i) for i in j] for j in inputs]
    return sum([flash(inputs) for i in range(100)])

#Part 2
def part2(inputs):
    inputs = [[int(i) for i in j] for j in inputs]
    t = 0
    while sum([sum([i for i in j]) for j in inputs]) != 0:
        flash(inputs)
        t += 1   
    return t

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))