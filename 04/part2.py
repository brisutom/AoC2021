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
win_state = [[False]*len(boards)]
for num in drawn:
    boards[boards == num] = -1
    all_boards_won = True
    new_win_state = [False]*len(boards)
    for idx, board in enumerate(boards):
        victory = check_victory(board)
        new_win_state[idx] = victory
        all_boards_won = all_boards_won and victory
    win_state.append(new_win_state)
    if all_boards_won:
        last_to_win_idx = np.array(win_state[-2]) ^ np.array(win_state[-1])
        print(sum(boards[last_to_win_idx][boards[last_to_win_idx] != -1]) * num)
        break
