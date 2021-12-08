# yeah this is really bad, but it works
from collections import defaultdict
from itertools import permutations


def decode(segments, values):
    for key in values:
        for perm in list(permutations(values[key])):
            if segments == "".join(perm):
                return str(key)


def construct_values(pre):
    values = defaultdict(lambda: set())
    correct = defaultdict(lambda: set())
    counts = defaultdict(lambda: 0)
    for segments in pre:
        num = None
        if len(segments) == 2:
            num = 1
        if len(segments) == 3:
            num = 7
        if len(segments) == 4:
            num = 4
        if len(segments) == 7:
            num = 8
        for letter in segments:
            counts[letter] += 1
        if num is not None:
            for letter in segments:
                values[num].add(letter)
    correct["a"] = list(values[7] - values[1])[0]
    correct["e"] = list(counts.keys())[list(counts.values()).index(4)]
    correct["g"] = list(values[8] - values[4] - set(correct["a"]) -
                        set(correct["e"]))[0]
    values[9] = list(values[4] | values[7] | set(correct["g"]))

    correct["b"] = list(counts.keys())[list(counts.values()).index(6)]
    correct["d"] = list(values[4] - values[1] - set(correct["b"]))[0]
    correct["f"] = list(counts.keys())[list(counts.values()).index(9)]
    correct["c"] = list(values[1] - set(correct["f"]))[0]

    # put numbers back together
    values[0] = list(values[8] - set(correct["d"]))
    values[6] = list(values[8] - set(correct["c"]))
    values[5] = list(values[8] - set(correct["e"]) - set(correct["c"]))
    values[2] = list(values[8] - set(correct["b"]) - set(correct["f"]))
    values[3] = list(values[8] - set(correct["b"]) - set(correct["e"]))
    values[1] = list(values[1])
    values[4] = list(values[4])
    values[7] = list(values[7])
    values[8] = list(values[8])
    return values


lines = [x.strip("\n").split(" | ") for x in open("input.txt").readlines()]
final_nums = []
for pre, post in lines:
    pre = pre.split(" ")
    post = post.split(" ")

    values = construct_values(pre)
    pre_nums = []
    for segments in post:
        pre_nums.append(decode(segments, values))

    final_nums.append(int("".join(pre_nums)))

print(sum(final_nums))
