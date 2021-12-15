# ugly solutions that takes like 10 minutes to run
import numpy as np


def get_neighbours(i, j, i_max, j_max):
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if i < i_max:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < j_max:
        neighbours.append((i, j+1))
    return neighbours


def minimum_risk(data):
    max_i, max_j = data.shape
    global M

    for i in range(0, max_i):
        for j in range(0, max_j):
            if i == 0 and j == 0:
                continue
            candidates = get_neighbours(i, j, max_i-1, max_j-1)
            min_risk = min(M[x] for x in candidates)
            M[i, j] = min_risk + data[i, j]
    return int(M[-1, -1])


data = [list(x.strip()) for x in open("input.txt").readlines()]
data = np.array(data, dtype=np.int32)

data_big = np.concatenate([data + x for x in range(5)], axis=1)
data_big[data_big > 9] -= 9
data_big = np.concatenate([data_big + x for x in range(5)], axis=0)
data_big[data_big > 9] -= 9

M = np.zeros(data_big.shape)
prev = 0
current = 1
while prev != current:
    prev = current
    current = minimum_risk(data_big)
print(current)
