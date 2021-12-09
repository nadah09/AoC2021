f = open("9.txt", "r")
f2 = open("9mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]
inputs = [[int(j) for j in i] for i in inputs]
miniinputs = [[int(j) for j in i] for i in miniinputs]

#Part 1
def isLow(i, j, graph):
    val = graph[i][j]
    u = graph[i][j-1] > val if j-1 >= 0 else True
    d = graph[i][j+1] > val if j+1 < len(graph[0]) else True
    l = graph[i-1][j] > val if i-1 >= 0 else True
    r = graph[i+1][j] > val if i+1 < len(graph) else True
    return u and d and l and r

def part1(graph):
    return sum([sum([graph[i][j]+1 if isLow(i, j, graph) else 0 for j in range(len(graph[0]))]) for i in range(len(graph))])

#Part 2
def findLowPoints(graph):
    return {(i, j) for i in range(len(graph)) for j in range(len(graph[0])) if isLow(i, j, graph)}

def findBasinSize(coord, graph):
    queue = [coord]
    seen = {coord}
    while queue:
        i, j = queue.pop()
        for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(graph) and 0 <= y < len(graph[0]):
                if graph[i][j] < graph[x][y] and (x, y) not in seen and graph[x][y] != 9:
                    queue.append((x, y))
                    seen.add((x, y))
    return len(seen)

def part2(graph):
    basins = {l: findBasinSize(l, graph) for l in findLowPoints(graph)}
    vals = sorted(basins.values())[::-1]
    return vals[0]*vals[1]*vals[2]

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))