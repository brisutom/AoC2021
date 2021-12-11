import numpy as np
num_flashed = 0


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

    # diagonal
    if i > 0 and j > 0:
        neighbours.append((i-1, j-1))
    if i > 0 and j < j_max:
        neighbours.append((i-1, j+1))
    if i < i_max and j > 0:
        neighbours.append((i+1, j-1))
    if i < i_max and j < j_max:
        neighbours.append((i+1, j+1))
    return neighbours


def step(data):
    global num_flashed
    flashed = np.full(data.shape, False)
    new_data = data + 1
    do_next = True
    while do_next:
        do_next = False
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                if new_data[i, j] > 9 and not flashed[i, j]:
                    neighbours = get_neighbours(i, j, len(data)-1, len(row)-1)
                    for neighbour in neighbours:
                        new_data[neighbour] += 1
                    flashed[i, j] = True
                    num_flashed += 1
                    do_next = True
    flashed[new_data > 9] = True
    new_data[flashed] = 0
    return new_data


data = [list(x.strip()) for x in open("input.txt").readlines()]
data = np.array(data, dtype=np.int32)
for _ in range(100):
    data = step(data)

print(num_flashed)
