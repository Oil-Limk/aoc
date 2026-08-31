import sys
from itertools import permutations

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

m = {}
cities = set()
for line in lines:
    a, _, b, _, d = line.split(" ")
    d = int(d)
    m[(a, b)] = d
    m[(b, a)] = d
    cities.add(a)
    cities.add(b)

max_d = 0
n = len(cities)

for perm in permutations(cities):
    s = 0
    for i in range(n - 1):
        s += m[(perm[i], perm[i + 1])]
    max_d = max(max_d, s)

print(max_d)
