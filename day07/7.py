f = open("7.txt", "r")
f2 = open("7mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

#Part 1
def part1(inputs):
    inputs = [int(i) for i in inputs[0].split(",")]
    minfuel = float("Inf")
    for i in range(min(inputs), max(inputs)):
        minfuel = min(sum([abs(j-i) for j in inputs]), minfuel) 
    return minfuel
    
#Part 2
def part2(inputs):
    inputs = [int(i) for i in inputs[0].split(",")]
    minfuel = float("Inf")
    for i in range(min(inputs), max(inputs)):
        minfuel = min(sum([abs(j-i)*(abs(j-i)+1)//2 for j in inputs]), minfuel) 
    return minfuel

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))