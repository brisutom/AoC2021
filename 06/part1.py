def tick(timers):
    new_timers = timers.copy()
    for i, timer in enumerate(timers):
        if timer == 0:
            new_timers[i] = 6
            new_timers.append(8)
        else:
            new_timers[i] -= 1
    return new_timers.copy()


timers = [int(x) for x in open("input.txt").readline().strip("\n").split(",")]

for _ in range(80):
    timers = tick(timers)

print(len(timers))
