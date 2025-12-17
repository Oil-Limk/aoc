import sys

lines = open(sys.argv[1]).read().strip()
sqrs = [[int(x) for x in line.split(',')] for line in lines.split('\n')]
m = len(sqrs)

result = 0
i = 0
while i < m:
  j = i + 1
  while j < m:
    xi, yi = sqrs[i]
    xj, yj = sqrs[j]
    a = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
    if a > result: result = a
    j += 1
  i += 1

print(result)
