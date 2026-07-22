import sys

lines = open(sys.argv[1]).read().strip()
manifold = list(map(list, lines.split('\n')))

m = len(manifold)
n = len(manifold[0])

result = 0

i = 1
while i < m:
  j = 0
  while j < n:
    if manifold[i-1][j] == 'S':
      if manifold[i][j] == '^':
        result += 1
        manifold[i][j-1] = 'S'
        manifold[i][j+1] = 'S'
      else:
        manifold[i][j] = 'S'
    j += 1
  i += 1

print(result)
