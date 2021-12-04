import numpy as np
data = [list(x.strip()) for x in open("input.txt").readlines()]
data = np.array(data, dtype=np.int32)
data_mean = data.mean(axis=0)
gamma = int("0b" + "".join("1" if x else "0" for x in data_mean > 0.5), 2)
epsilon = int("0b" + "".join("1" if x else "0" for x in data_mean < 0.5), 2)
print(gamma*epsilon)
