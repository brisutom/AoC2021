steps = [x.strip().split(" ") for x in open("input.txt").readlines()]
x = 0
depth = 0
for step in steps:
    com, units = step
    units = int(units)
    if com == "forward":
        x += units
    elif com == "down":
        depth += units
    elif com == "up":
        depth -= units

print(x*depth)
