import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

result = 0
for l in lines:
    lint = [int(i) for i in l.split("x")]
    bow = 1
    for a in lint:
        bow *= a
    result += bow
    result += 2 * min(a + b for a, b in combinations(lint, 2))
print(result)
