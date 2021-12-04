numbers = [int(x) for x in open("input.txt").readlines()]
shifted = numbers.copy()
shifted.pop(0)
shifted2 = shifted.copy()
shifted2.pop(0)

sums = list(map(sum, zip(numbers, shifted, shifted2)))
sums_shifted = sums.copy()
sums_shifted.append(sums_shifted.pop(0))
diffs = list(map(lambda x: x[1]-x[0], zip(sums, sums_shifted)))
increases = [x for x in diffs if x > 0]
print(len(increases))
