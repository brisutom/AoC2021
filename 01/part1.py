numbers = [int(x) for x in open("input.txt").readlines()]
shifted = numbers.copy()
shifted.append(shifted.pop(0))
diffs = list(map(lambda x: x[1]-x[0], zip(numbers, shifted)))
increases = [x for x in diffs if x > 0]
print(len(increases))
