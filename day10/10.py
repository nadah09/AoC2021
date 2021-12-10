from collections import defaultdict

f = open("10.txt", "r")
f2 = open("10mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n")]
miniinputs = [i.strip() for i in f2.read().split("\n")]

#Part 1
def part1(inputs):
    match = {"]": "[", "}": "{", ")": "(", ">": "<"}
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    s = 0
    for line in inputs:
        stack = []
        for val in line:
            if val in "{[(<":
                stack.append(val)
            else:
                if stack.pop() != match[val]:
                    s += score[val]
                    break
    return s

#Part 2
def part2(inputs):
    score = {"(": 1, "[": 2, "{": 3, "<": 4}
    match = {"]": "[", "}":"{", ")": "(", ">":"<"}
    scores = []
    for line in inputs:
        stack = []
        for val in line:
            if val in "{[(<":
                stack.append(val)
            else:
                if stack.pop() != match[val]:
                    continue
        scores.append(sum([score[stack[i]]*5**i for i in range(len(stack))]))
    return sorted(scores)[len(scores)//2]

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))