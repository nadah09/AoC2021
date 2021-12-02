f = open("2.txt", "r")
f2 = open("2mini.txt", "r")
inputs = [i.strip().split() for i in f]
miniinputs = [i.strip().split() for i in f2]

#Part 1
def part1(inputs):
    x, y = 0, 0
    for i in inputs:
        d, amt = i[0], int(i[1])
        if d == "forward":
            x += amt
        elif d == "down":
            y += amt
        elif d == "up":
            y -= amt
    return x*y
    
#Part 2
def part2(inputs):
    x, y, aim = 0, 0, 0
    for i in inputs:
        d, amt = i[0], int(i[1])
        if d == "forward":
            x += amt
            y += aim*amt
        elif d == "down":
            aim += amt
        elif d == "up":
            aim -= amt
    return x*y

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))