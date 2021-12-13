f = open("13.txt", "r")
f2 = open("13mini.txt", "r")
inputs = [i for i in f.read().split("\n\n")]
miniinputs = [i for i in f2.read().split("\n\n")]

#Part 1
def fold(inputs, first = False):
    pts = {(int(i.split(",")[0]), int(i.split(",")[1])) for i in inputs[0].split("\n")}
    dirs = [j.split("=") for j in [i.split(" ")[2] for i in inputs[1].split("\n")]]
    for axis, num in dirs:
        num = int(num)
        newpts = set()
        for x, y in pts:
            if axis == "x" and x > num:
                newpts.add((2*num-x, y))
            elif axis == "y" and y > num:
                newpts.add((x, 2*num-y))
            else:
                newpts.add((x, y))
        pts = newpts
        if first:
            break
    return pts

def part1(inputs):
    return len(fold(inputs, True))

#Part 2
def part2(inputs):
    pts = fold(inputs)
    for y in range(max([i[1] for i in pts])+1):
        r = ''
        for x in range(max([i[0] for i in pts])+1):
            r += "#" if (x, y) in pts else " "
        print(r)

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ", part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))