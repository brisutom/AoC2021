# naive solution, will not work for part2
from collections import Counter


def do_replace(template, trans_dict):
    template_shifted = template[1:]
    result = template[:1]
    for i in range(len(template_shifted)):
        pair = template[i] + template_shifted[i]
        if pair in trans_dict:
            result = result[:-1] + trans_dict[pair]
        else:
            result = result + pair

    return result


lines = [x.strip("\n") for x in open("input.txt") if x != "\n"]
template = lines.pop(0)
lines = [x.split(" -> ") for x in lines]
replacement = ["".join([a[0], b[0], a[1]]) for a, b in lines]
original = [x for x, _ in lines]
trans_dict = dict(zip(original, replacement))

# part 1
for _ in range(10):
    template = do_replace(template, trans_dict)
counts = Counter(template)
print(max(counts.values()) - min(counts.values()))
