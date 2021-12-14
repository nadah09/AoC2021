from collections import defaultdict

f = open("14.txt", "r")
f2 = open("14mini.txt", "r")
inputs = [i for i in f.read().split("\n\n")]
miniinputs = [i for i in f2.read().split("\n\n")]

#Part 1
def pairInsert(inputs, iters):
    code, rules = inputs[0], [i.split(" -> ") for i in inputs[1].split("\n")]
    rules = {i[0]: i[1] for i in rules}
    countP = defaultdict(int, {code[i:i+2]: code.count(code[i:i+2]) for i in range(len(code)-1)})
    countC = defaultdict(int, {i: code.count(i) for i in set(code)})
    for n in range(iters):
        copyP = defaultdict(int, {k : v for k, v in countP.items()})
        for p, c in countP.items():
            if p in rules:
                copyP[p] -= c
                copyP[p[0] + rules[p]] += c
                copyP[rules[p] + p[1]] += c
                countC[rules[p]] += c
        countP = copyP
    return max(countC.values()) - min(countC.values())

def part1(inputs):
    return pairInsert(inputs, 10)

#Part 2
def part2(inputs):
    return pairInsert(inputs, 40)

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ", part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))