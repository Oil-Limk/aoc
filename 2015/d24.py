import sys
from itertools import combinations

from numpy import inf

with open(sys.argv[1]) as f:
    ns = [int(x) for x in f.read().strip().split("\n")]

weight = sum(ns) // 4


def prod(l):
    a = 1
    for x in l:
        a *= x
    return a


result = (None, inf)
for i in range(1, len(ns) - 1):
    for c in combinations(ns, i):
        if sum(c) == weight:
            p = prod(c)
            if p < result[1]:
                result = (c, p)
    if result[0] is not None:
        break

print(result[1])
