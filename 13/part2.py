import matplotlib.pyplot as plt
import numpy as np


def do_fold(fold, paper):
    d, val = fold
    folded = []
    for x, y in paper:
        if d == "y":
            if y > val:
                folded.append((x, 2*val-y))
            else:
                folded.append((x, y))
        elif d == "x":
            if x > val:
                folded.append((2*val-x, y))
            else:
                folded.append((x, y))
    return set(folded)


paper = [[int(y) for y in x.strip("\n").split(",")] for x in open("input.txt") if x != "\n" and x[0] != "f"]
folds = [x.strip("\n").split(" ")[-1].split("=") for x in open("input.txt") if x[0] == "f"]
folds = [(d, int(val)) for d, val in folds]


for fold in folds:
    paper = do_fold(fold, paper)

max_x = max(x for x, _ in paper) + 1
max_y = max(y for _, y in paper) + 1
res = np.zeros((max_x, max_y))
np.add.at(res, tuple(zip(*paper)), 1)
res = np.rot90(res)
plt.imshow(res)
plt.gca().invert_yaxis()
plt.show()
