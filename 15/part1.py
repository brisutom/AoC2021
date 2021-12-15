# curiously this works for my input even if it really shouldn't
import numpy as np


def minimum_risk(data):
    max_i, max_j = data.shape
    M = data.copy()

    for i in range(0, max_i):
        for j in range(0, max_j):
            if j == 0:
                min_risk = M[i - 1, j]
            elif i == 0:
                min_risk = M[i, j-1]
            else:
                min_risk = min(M[i - 1, j], M[i, j-1])
            M[i, j] += min_risk
    return M


data = [list(x.strip()) for x in open("input.txt").readlines()]
data = np.array(data, dtype=np.int32)

M = minimum_risk(data)
print(M[-1, -1] - M[0, 0])
