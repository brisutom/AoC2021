lines = [x.strip("\n") for x in open("input.txt").readlines()]
points = dict(zip((None, ")", "]", "}", ">"), (0, 3, 57, 1197, 25137)))


def find_corrupted(line):
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    pairs = dict(zip(open_tup, close_tup))
    queue = []
    for ch in line:
        if ch in open_tup:
            queue.append(pairs[ch])
        elif ch in close_tup:
            if ch != queue.pop():
                return ch


result = sum([points[find_corrupted(line)] for line in lines])
print(result)
