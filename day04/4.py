f = open("4.txt", "r")
f2 = open("4mini.txt", "r")
inputs = [i.strip() for i in f.read().split("\n\n")]
miniinputs = [i.strip() for i in f2.read().split("\n\n")]

#Part 1
def part1(inputs):
    nums, boards = [int(i) for i in inputs[0].split(",")], inputs[1:]
    boards = [[i.split() for i in x.split("\n")] for x in boards]
    found = [[[False for i in range(len(board))] for j in range(len(board[0]))] for board in boards]
    for n in nums:
        for m in range(len(boards)):
            board = boards[m]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if int(board[i][j]) == n:
                        found[m][i][j] = True
            for i in range(len(found[m])):
                if all([found[m][i][x] for x in range(len(found[m]))]) or all([found[m][x][i] for x in range(len(found[m]))]):
                    s = sum([sum([int(boards[m][i][j]) if not found[m][i][j] else 0 for i in range(len(board))]) for j in range(len(board[0]))])
                    return s*n
#Part 2
def part2(inputs):
    nums, boards = [int(i) for i in inputs[0].split(",")], inputs[1:]
    boards = [[i.split() for i in x.split("\n")] for x in boards]
    found = [[[False for i in range(len(board))] for j in range(len(board[0]))] for board in boards]
    seen = set()
    scores = []
    for n in nums:
        for m in range(len(boards)):
            board = boards[m]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if int(board[i][j]) == n:
                        found[m][i][j] = True
            if m in seen:
                continue
            for i in range(len(found[m])):
                if all([found[m][i][x] for x in range(len(found[m]))]) or all([found[m][x][i] for x in range(len(found[m]))]):
                    s = sum([sum([int(boards[m][i][j]) if not found[m][i][j] else 0 for i in range(len(board))]) for j in range(len(board[0]))])
                    scores.append(s*n)
                    seen.add(m)
    return scores[-1]

print("REAL PART 1: ", part1(inputs))
print("MINI PART 1: ",part1(miniinputs))

print("REAL PART 2: ", part2(inputs))
print("MINI PART 2: ", part2(miniinputs))