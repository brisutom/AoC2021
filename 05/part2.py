from collections import defaultdict


def addPoints(a, b):
    return tuple(map(lambda x, y: x+y, a, b))


def coords_to_line(p1, p2):
    if p1[1] == p2[1]:
        if p2[0] > p1[0]:
            new_points = list(map((lambda new: addPoints(p1, new)), [(x, 0) for x in range(p2[0]-p1[0]+1)]))
        else:
            new_points = list(map((lambda new: addPoints(p1, new)), [(-x, 0) for x in range(p1[0]-p2[0]+1)]))
        return new_points

    elif p1[0] == p2[0]:
        if p2[1] > p1[1]:
            new_points = list(map((lambda new: addPoints(p1, new)), [(0, x) for x in range(p2[1]-p1[1]+1)]))
        else:
            new_points = list(map((lambda new: addPoints(p1, new)), [(0, -x) for x in range(p1[1]-p2[1]+1)]))
        return new_points

    elif p2[0] > p1[0]:
        if p2[1] > p1[1]:
            new_points = list(map((lambda new: addPoints(p1, new)), [(x, x) for x in range(p2[1]-p1[1]+1)]))
        else:
            new_points = list(map((lambda new: addPoints(p1, new)), [(x, -x) for x in range(p1[1]-p2[1]+1)]))
        return new_points

    elif p1[0] > p2[0]:
        if p2[1] > p1[1]:
            new_points = list(map((lambda new: addPoints(p1, new)), [(-x, x) for x in range(p2[1]-p1[1]+1)]))
        else:
            new_points = list(map((lambda new: addPoints(p1, new)), [(-x, -x) for x in range(p1[1]-p2[1]+1)]))
        return new_points


lines = [x.strip("\n").split(" -> ") for x in open("input.txt").readlines()]
map_lines = defaultdict(lambda: 0)
for i, (p1, p2) in enumerate(lines):
    p1 = [int(x) for x in p1.split(",")]
    p2 = [int(x) for x in p2.split(",")]
    line = coords_to_line(p1, p2)
    if line is None:
        continue
    for point in line:
        map_lines[point] += 1

print(sum(value >= 2 for value in map_lines.values()))
