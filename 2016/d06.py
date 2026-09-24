import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

acc = [""] * 8

for l in lines:
    for i, s in enumerate(l):
        acc[i] += s

result = ""
for a in acc:
    la = list(a)
    la.sort(key=a.count)
    result += la[0]

print(result)
