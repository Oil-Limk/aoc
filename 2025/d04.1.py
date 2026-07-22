import sys

lines = open(sys.argv[1]).read().strip()
floor = lines.split('\n')

result = 0

m = len(floor)
n = len(floor[0])

for i in range(m):
  for j in range(n):
    if floor[i][j] == '@':
      ns = 0
      ii = max(0, i - 1)
      im = min(m, i + 2)
      while ii < im:
        jj = max(0, j - 1)
        jm = min(n, j + 2)
        while jj < jm:
          if (ii != i or jj != j) and floor[ii][jj] == '@':
            ns += 1
          jj += 1
        ii += 1
      if ns < 4:
        result += 1

print(result)
