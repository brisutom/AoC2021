from statistics import median
lines = [x.strip("\n") for x in open("input.txt").readlines()]
points = dict(zip((")", "]", "}", ">"), (1, 2, 3, 4)))


def is_corrupted(line):
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    pairs = dict(zip(open_tup, close_tup))
    queue = []
    for ch in line:
        if ch in open_tup:
            queue.append(pairs[ch])
        elif ch in close_tup:
            if ch != queue.pop():
                return True
    return False


def complete(line):
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    pairs = dict(zip(open_tup, close_tup))
    queue = []
    for ch in line:
        if ch in open_tup:
            queue.append(pairs[ch])
        elif ch in close_tup:
            queue.pop()
    return list(reversed(queue))


incomplete = [line for line in lines if not is_corrupted(line)]
total_score = []
for line in incomplete:
    score = 0
    to_complete = complete(line)
    for ch in to_complete:
        score *= 5
        score += points[ch]
    total_score.append(score)

print(median(total_score))
