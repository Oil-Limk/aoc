import sys

lines = open(sys.argv[1]).read().strip()
points = [[int(x) for x in line.split(',')] for line in lines.split('\n')]
m = len(points)

rectangles = []

i = 0
while i < m:
  j = i + 1
  while j < m:
    xi, yi = points[i]
    xj, yj = points[j]
    a = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
    rectangles.append([i, j, a])
    j += 1
  i += 1

rectangles.sort(key=lambda x : x[-1], reverse=True)

result = 0

for i, j, a in rectangles:
  xi, yi = points[i]
  xj, yj = points[j]
  xmin = min(xi, xj)
  xmax = max(xi, xj)
  ymin = min(yi, yj)
  ymax = max(yi, yj)

  valid = True
  pi2pj = 0
  pj2pi = 0
  k = i
  while k != j:
    xk1, yk1 = points[k]
    xk2, yk2 = points[(k+1) % m]
    if xk1 == xk2:
      if xmin < xk1 < xmax:
        if (yk1 > ymin or yk2 > ymin) and (yk1 < ymax or yk2 < ymax):
          valid = False
          break
    if yk1 == yk2:
      if ymin < yk1 < ymax:
        if (xk1 > xmin or xk2 > xmin) and (xk1 < xmax or xk2 < xmax):
          valid = False
          break
    k = (k + 1) % m
  if valid:
    while k != i:
      xk1, yk1 = points[k]
      xk2, yk2 = points[(k+1) % m]
      if xk1 == xk2:
        if xmin < xk1 < xmax:
          if (yk1 > ymin or yk2 > ymin) and (yk1 < ymax or yk2 < ymax):
            valid = False
            break
      if yk1 == yk2:
        if ymin < yk1 < ymax:
          if (xk1 > xmin or xk2 > xmin) and (xk1 < xmax or xk2 < xmax):
            valid = False
            break
      k = (k + 1) % m
  if a > result and valid:
    result = a

print(result)
