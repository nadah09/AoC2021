f = open("15.txt", "r")
f2 = open("15mini.txt", "r")
inputs = [i for i in f.read().split("\n")]
miniinputs = [i for i in f2.read().split("\n")]

#Part 1
def findPath(inputs):
    queue = [(0, 0, 0)]
    dists = {}
    while queue:
        score, x, y = queue.pop(0)
        if x == len(inputs)-1 and y == len(inputs[0])-1:
            return score
        for nx, ny in [(x, y+1), (x+1, y), (x-1, y), (x, y-1)]:
            if 0 <= nx < len(inputs) and 0 <= ny < len(inputs[0]):
                nScore = score+inputs[nx][ny]
                if (nx, ny) not in dists or dists[(nx, ny)] > nScore:
                    dists[(nx, ny)] = nScore
                    queue.append((nScore, nx, ny))
        queue = sorted(queue)
    return

def part1(inputs):
    inputs = [[int(i) for i in j] for j in inputs]
    return findPath(inputs)

#Part 2
def expand(inputs):
    exp = [[i for i in 5*j] for j in 5*inputs]
    for x in range(len(exp)):
        for y in range(len(exp[0])):
            toAdd = x//len(inputs) + y//len(inputs[0])
            exp[x][y] = (exp[x][y] + toAdd-1)%9+1
    return exp


def part2(inputs):
    inputs = [[int(i) for i in j] for j in inputs]
    return findPath(expand(inputs))

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ", part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))