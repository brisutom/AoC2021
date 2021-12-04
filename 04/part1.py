import numpy as np


def check_victory(board):
    for row in board:
        if sum(row) == -5:
            return True
    for col in board.T:
        if sum(col) == -5:
            return True
    return False


lines = [x.strip("\n") for x in open("input.txt").readlines()]
drawn = [int(x) for x in lines[0].split(",")]
boards = []
board = []
for line in lines[2:]:
    if line != "":
        board.append([int(x) for x in line.replace("  ", " ").lstrip().split(" ")])
    else:
        boards.append(board)
        board = []
else:
    boards.append(board)

boards = np.array(boards)

for num in drawn:
    boards[boards == num] = -1
    for board in boards:
        victory = check_victory(board)
        if victory:
            print(board)
            print(sum(board[board != -1]) * num)
            break
    if victory:
        break
