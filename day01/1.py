f = open("1.txt", "r")
inputs = [int(i) for i in f]

#Part 1
def countLarger(inputs):
    return sum([1 if inputs[i] > inputs[i-1] else 0 for i in range(1, len(inputs))])

#Part 2
def countLargerWindow(inputs):
    return sum([1 if sum(inputs[i:i+3]) > sum(inputs[i-1:i-1+3]) else 0 for i in range(1, len(inputs)-2)])

print(countLarger(inputs))
print(countLargerWindow(inputs))