f = open("25.txt", "r")
f2 = open("25mini.txt", "r")
inputs = [i for i in f.read().split("\n")]
miniinputs = [i for i in f2.read().split("\n")]

#Part 1
def stepDir(inputs, d):
    sym = ">" if d == (0, 1) else "v"
    moved = {(i, j) for i in range(len(inputs)) for j in range(len(inputs[0])) 
        if inputs[i][j] == sym and inputs[(i+d[0])%len(inputs)][(j+d[1])%len(inputs[0])] == "."}
    for i, j in moved:
        inputs[i][j] = "."
        inputs[(i+d[0])%len(inputs)][(j+d[1])%len(inputs[0])] = sym
    return inputs, len(moved)

def step(inputs):
    inputs, move1 = stepDir(inputs, (0, 1)) #east steps
    inputs, move2 = stepDir(inputs, (1, 0)) #south steps
    return inputs, move1+move2

def part1(inputs):
    inputs = [[j for j in i] for i in inputs]
    i = 0
    while True:
        i += 1
        inputs, moved = step(inputs)
        if moved == 0:
            return i

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ", part1(miniinputs))