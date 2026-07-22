import sys
from itertools import combinations 

lines = open(sys.argv[1]).readlines()

result = 0
for l in lines:
  ps = [ a * b for a, b in combinations((int(i) for i in l.split('x')), 2) ]
  result += 2 * sum(ps) + min(ps)
print(result)
