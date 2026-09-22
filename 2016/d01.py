import sys

import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().strip().split(", ")

ds = [np.array((0, 1)), np.array((-1, 0)), np.array((0, -1)), np.array((1, 0))]
p = np.array((0, 0))
v = {}
d = 0

for s in lines:
    if s[0] == "L":
        d += 1
    else:
        d -= 1
    d %= 4
    for _ in range(int(s[1:])):
        p += ds[d]
        if str(p) in v:
            break
        v[str(p)] = None
    else:
        continue
    break
print(abs(p[0]) + abs(p[1]))
