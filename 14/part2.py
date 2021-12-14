from collections import Counter
from collections import defaultdict


def counts_pairs_to_letters(pairs_counts):
    letters_counts = defaultdict(lambda: 0)
    for key in pairs_counts:
        letters_counts[key[1]] += pairs_counts[key]
    return letters_counts


def do_step(pairs_counts, trans_dict):
    new_pairs_counts = pairs_counts.copy()
    for pair in pairs_counts:
        if pair in trans_dict:
            new_pairs_counts[pair[0] + trans_dict[pair]] += pairs_counts[pair]
            new_pairs_counts[trans_dict[pair] + pair[1]] += pairs_counts[pair]
            new_pairs_counts[pair] -= pairs_counts[pair]
    return new_pairs_counts


lines = [x.strip("\n") for x in open("input.txt") if x != "\n"]
template = lines.pop(0)
lines = [x.split(" -> ") for x in lines]
trans_dict = dict(lines)

pairs_counts = Counter(["".join(x) for x in zip(template, template[1:])])


for _ in range(41):
    letter_counts = counts_pairs_to_letters(pairs_counts)
    letter_counts[template[0]] += 1
    pairs_counts = do_step(pairs_counts, trans_dict)

print(max(letter_counts.values()) - min(letter_counts.values()))
