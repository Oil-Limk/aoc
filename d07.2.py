import sys

lines = open(sys.argv[1]).read().strip().replace('.', '0').replace('S', '1')
manifold = [[int(s) if s.isdigit() else s for s in line] for line in lines.split('\n')]

m = len(manifold)
n = len(manifold[0])

result = 0

i = 1
while i < m:
  j = 0
  while j < n:
    s = manifold[i-1][j]
    if s != '^':
      if manifold[i][j] == '^':
        manifold[i][j-1] += s
        manifold[i][j+1] += s
      else:
        manifold[i][j] += s
    j += 1
  i += 1

result = sum(manifold[-1])

print(result)
