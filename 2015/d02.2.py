import sys
from itertools import combinations

lines = open(sys.argv[1]).readlines()

result = 0
for l in lines:
  lint = [ int(i) for i in l.split('x') ]
  bow = 1
  for a in lint:
    bow *= a
  result += bow
  result += 2 * min( a + b for a, b in combinations(lint, 2) )
print(result)
