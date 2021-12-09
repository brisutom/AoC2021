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


def find_basin(i, j, data, basin):
    basin.append((i, j))
    neighbours = get_neighbours(i, j, len(data)-1, len(row)-1)
    for neighbour in neighbours:
        if data[neighbour] != 9 and neighbour not in basin:
            basin.append(find_basin(neighbour[0], neighbour[1], data, basin))
    return basin


data = [list(x.strip("\n")) for x in open("input.txt").readlines()]
data = np.array(data, dtype=np.int32)

basin_lens = []
for i, row in enumerate(data):
    for j, col in enumerate(row):
        neighbours = get_neighbours(i, j, len(data)-1, len(row)-1)
        neighbours_values = [data[x] for x in neighbours]
        if data[i, j] < min(neighbours_values):
            basin = find_basin(i, j, data, [])
            basin = [x for x in basin if type(x) is tuple]
            basin_lens.append(len(basin))

print(np.prod(sorted(basin_lens, reverse=True)[:3]))
