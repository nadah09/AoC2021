f = open("3.txt", "r")
f2 = open("3mini.txt", "r")
inputs = [i.strip() for i in f]
miniinputs = [i.strip() for i in f2]

#Part 1
def part1(inputs):
    g = ""
    e = ""
    for i in range(len(inputs[0])):
        bits = [x[i] for x in inputs]
        if bits.count("1") >= bits.count("0"):
            g+= "1"
            e += "0"
        else:
            g+="0"
            e+="1"
    return int(g, 2)*int(e, 2)
    
#Part 2
def findNum(inputs, ma, mi):
    nums = [i for i in inputs]
    for i in range(len(inputs[0])):
        bits = [x[i] for x in nums]
        if bits.count("1") >= bits.count("0"):
            nums = [x for x in nums if x[i] == mi]
        else:
            nums = [x for x in nums if x[i] == ma]
        try:
            result = nums[0]
        except:
            break
    return int(result, 2)

def part2(inputs):
    return findNum(inputs, "0", "1")*findNum(inputs, "1", "0")

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))