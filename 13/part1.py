def do_fold(fold, paper):
    d, val = fold
    folded = []
    for x, y in paper:
        if d == "y":
            if y > val:
                folded.append((x, 2*val-y))
            else:
                folded.append((x, y))
        elif d == "x":
            if x > val:
                folded.append((2*val-x, y))
            else:
                folded.append((x, y))
    return set(folded)


paper = [[int(y) for y in x.strip("\n").split(",")] for x in open("input.txt") if x != "\n" and x[0] != "f"]
folds = [x.strip("\n").split(" ")[-1].split("=") for x in open("input.txt") if x[0] == "f"]
folds = [(d, int(val)) for d, val in folds]

folded = do_fold(folds[0], paper)
print(len(folded))
