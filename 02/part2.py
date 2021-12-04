steps = [x.strip().split(" ") for x in open("input.txt").readlines()]
x = 0
depth = 0
aim = 0
for com, units in steps:
    units = int(units)
    if com == "forward":
        x += units
        depth += aim*units
    elif com == "down":
        aim += units
    elif com == "up":
        aim -= units

print(x*depth)
