import sys
from itertools import combinations
lines = open(sys.argv[1]).readlines()
containers = list(map(int, lines))
result = 0
for i in range(len(lines)):
  for comb in combinations(containers, i):
    if sum(comb) == 150:
      result += 1
print(result)
