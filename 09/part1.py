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


data = [list(x.strip("\n")) for x in open("input.txt").readlines()]
data = np.array(data, dtype=np.int32)

low_points = []
for i, row in enumerate(data):
    for j, col in enumerate(row):
        neighbours = get_neighbours(i, j, len(data)-1, len(row)-1)
        neighbours_values = [data[x] for x in neighbours]
        if data[i, j] < min(neighbours_values):
            low_points.append(data[i, j])

print(sum(x+1 for x in low_points))
