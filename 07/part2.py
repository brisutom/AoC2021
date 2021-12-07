pos = [int(x) for x in open("input.txt").readline().split(",")]
distances = []
for line in range(max(pos)):
    dist = [sum(range(abs(line - x)+1)) for x in pos]
    distances.append(sum(dist))

print(min(distances))
