import sys

lines = open(sys.argv[1]).read().strip()
nodes = [[int(x) for x in line.split(',')]+[-1] for line in lines.split('\n')]
m = len(nodes)

edges = []
i = 0

while i < m:
  j = i + 1
  while j < m:
    xi, yi, zi, _ = nodes[i]
    xj, yj, zj, _ = nodes[j]
    d = (xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2
    edges.append([i, j, d])
    j += 1
  i += 1

edges.sort(key = lambda l : l[2])

circuits = []
pairs = 1000
ei = 0
while ei < pairs:
  i, j, _ = edges[ei]
  ci = nodes[i][3]
  cj = nodes[j][3]
  if ci == -1 and cj == -1:
    nodes[i][3] = nodes[j][3] = len(circuits)
    circuits.append([i, j])
  elif ci != cj:
    if ci == -1:
      nodes[i][3] = cj
      circuits[cj].append(i)
    elif cj == -1:
      nodes[j][3] = ci
      circuits[ci].append(j)
    else:
      # merge
      for k in circuits[cj]:
        nodes[k][3] = ci
        circuits[ci].append(k)
      circuits[cj].clear()
  ei += 1

lcs = [len(c) for c in circuits]
lcs.sort(reverse=True)

result = 1
for lc in lcs[:3]:
  result *= lc

print(result)
