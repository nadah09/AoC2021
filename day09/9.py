f = open("9.txt", "r")
f2 = open("9mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

#Part 1
def islow(i, j, graph):
    val = graph[i][j]
    u = graph[i][j-1] > val if j-1 >= 0 else True
    d = graph[i][j+1] > val if j+1 < len(graph[0]) else True
    l = graph[i-1][j] > val if i-1 >= 0 else True
    r = graph[i+1][j] > val if i+1 < len(graph) else True
    if u and d and l and r:
        return True
    return False

def part1(inputs):
    graph = [[int(j) for j in i] for i in inputs]
    s = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if islow(i, j, graph):
                s += graph[i][j]+1
    return s

#Part 2
def low(inputs):
    graph = [[int(j) for j in i] for i in inputs]
    low = set()
    s = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if islow(i, j, graph):
                low.add((i, j))
    return low

def findbasin(coord, graph):
    queue = [coord]
    seen = set()
    while queue:
        i, j = queue.pop()
        seen.add((i, j))
        for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(graph) and 0 <= y < len(graph[0]):
                if graph[i][j] < graph[x][y] and (x, y) not in seen and graph[x][y] != 9:
                    queue.append((x, y))
                    seen.add((x, y))
    print(seen)
    return len(seen)

def part2(inputs):
    graph = [[int(j) for j in i] for i in inputs]
    lowpoints = low(inputs)
    d = {low: 0 for low in lowpoints}
    for point in lowpoints:
        d[point] = findbasin(point, graph)
    vals = sorted(d.values())[::-1]
    print(vals)
    return vals[0]*vals[1]*vals[2]

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))