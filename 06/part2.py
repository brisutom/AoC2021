from collections import Counter


def tick(timers):
    timer_zero = timers[0]
    for time in range(0, 8):
        timers[time] = timers[time+1]
    timers[8] = timer_zero
    timers[6] += timer_zero
    return timers


timers = [int(x) for x in open("input.txt").readline().strip("\n").split(",")]
timers = Counter(timers)
for _ in range(256):
    timers = tick(timers)

print(sum(timers.values()))
