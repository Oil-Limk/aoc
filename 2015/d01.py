import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()

n = 0
p = 0
for i in lines:
    p += 1
    if i == "(":
        n += 1
    else:
        n -= 1
    if n < 0:
        break
print(p)
