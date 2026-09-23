import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

result = 0
m = 0
s = 0

for i, l in enumerate(lines):
    n = int(l[:5])
    if n > m:
        s += m
        m = n
    else:
        s += n
    if i % 3 == 2:
        if s > m:
            result += 1
        m = 0
        s = 0

for i, l in enumerate(lines):
    n = int(l[5:10])
    if n > m:
        s += m
        m = n
    else:
        s += n
    if i % 3 == 2:
        if s > m:
            result += 1
        m = 0
        s = 0

for i, l in enumerate(lines):
    n = int(l[10:])
    if n > m:
        s += m
        m = n
    else:
        s += n
    if i % 3 == 2:
        if s > m:
            result += 1
        m = 0
        s = 0

print(result)
