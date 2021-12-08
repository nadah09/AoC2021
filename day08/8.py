f = open("8.txt", "r")
f2 = open("8mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

#Part 1
def part1(inputs):
    counts = [2, 3, 4, 7]
    c = 0
    for i in inputs:
        first, second = i.split("|")
        c += sum([len(j) in counts for j in second.split()])
    return c

def findCode(codes):
    nums = {}
    counts = {7: 8, 2: 1, 3: 7, 4: 4}
    codes = [''.join(sorted(j)) for j in codes.split()]
    for j in codes:
        if len(j) in counts:
            nums[counts[len(j)]] = j
    for j in codes:
        inter1 = set(nums[1]).intersection(set(j))
        inter4 = set(nums[4]).intersection(set(j))
        if len(j) == 6:
            if len(inter1) == 1:
                nums[6] = j
            elif len(inter4) == 4:
                nums[9] = j
            else:
                nums[0] = j
        elif len(j) == 5:
            if len(inter1) == 2:
                nums[3] = j
            elif len(inter4) == 2:
                nums[2] = j
            else:
                nums[5] = j 
    return dict((v,k) for k,v in nums.items())

#Part 2
def part2(inputs):
    c = 0
    for i in inputs:
        first, second = i.split("|")
        nums = findCode(first)
        t = ''.join([str(nums[''.join(sorted(j))]) for j in second.split()])
        c += int(t)  
    return c

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))