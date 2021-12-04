import numpy as np
data = [list(x.strip()) for x in open("input.txt").readlines()]
data = np.array(data, dtype=np.int32)

to_keep = [True]*data.shape[0]
for col in data.T:
    if len(data[to_keep, :]) == 1:
        co2 = data[to_keep, :][0]
        break
    col_mean = col[to_keep].mean()
    if col_mean >= 0.5:
        to_keep = to_keep & (col == 0)
    else:
        to_keep = to_keep & (col == 1)

to_keep = [True]*data.shape[0]
for col in data.T:
    col_mean = col[to_keep].mean()
    if col_mean >= 0.5:
        to_keep = to_keep & (col == 1)
    else:
        to_keep = to_keep & (col == 0)
    if len(data[to_keep, :]) == 1:
        ox = data[to_keep, :][0]
        break

ox = int("0b" + "".join("1" if x else "0" for x in ox), 2)
co2 = int("0b" + "".join("1" if x else "0" for x in co2), 2)
print(ox*co2)
