import sys
from itertools import combinations
lines = open(sys.argv[1]).readlines()
containers = list(map(int, lines))
result = 0
stop = False
for i in range(len(lines)):
  for comb in combinations(containers, i):
    if sum(comb) == 150:
      stop = True
      result += 1
  if stop: break
print(result)
