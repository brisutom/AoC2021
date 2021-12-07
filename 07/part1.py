pos = [int(x) for x in open("input.txt").readline().split(",")]
distances = []
for line in range(max(pos)):
    dist = [abs(line - x) for x in pos]
    distances.append(sum(dist))

print(min(distances))
