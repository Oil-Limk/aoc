import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    line = f.read().strip()

n = int(line)


def prod(l):
    a = 1
    for x in l:
        a *= x
    return a


def sum_of_facts(m):
    sqrt_m = int(m**0.5)
    f = []
    j = m
    for i in range(2, sqrt_m):
        while j % i == 0:
            j //= i
            f.append(i)
    s = 0
    for i in range(len(f) + 1):
        for c in set(combinations(f, i)):
            p = prod(c)
            if m // p <= 50:
                s += p * 11
    return s


for i in range(n // 11 + 1):
    if n <= sum_of_facts(i):
        print(i)
        break
