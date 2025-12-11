import sys

lines = open(sys.argv[1]).read().strip()
floor = list(map(lambda x : list(x), lines.split('\n')))

m = len(floor)
n = len(floor[0])

result = 0
loop = True

while loop:
  loop = False
  rmr = []
  for i in range(m):
    for j in range(n):
      if floor[i][j] == '@':
        nr = 0
        ii = max(0, i - 1)
        im = min(m, i + 2)
        while ii < im:
          jj = max(0, j - 1)
          jm = min(n, j + 2)
          while jj < jm:
            if (ii != i or jj != j) and floor[ii][jj] == '@':
              nr += 1
            jj += 1
          ii += 1
        if nr < 4:
          rmr += [(i, j)]
          result += 1
          loop = True
  for i, j in rmr:
    floor[i][j] = '.'

print(result)
