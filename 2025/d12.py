import re
import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()

*presents, areas = lines.split("\n\n")

result = 0
for sa in areas.split("\n"):
    a, b, *ns = map(int, re.findall("\\d+", sa))
    if a * b < sum(p.count("#") * n for p, n in zip(presents, ns)):
        continue
    result += 1

print(result)
