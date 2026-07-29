import sys
import numpy as np
from itertools import permutations

lines = open(sys.argv[1]).readlines()
delta_happiness = np.zeros((8,8), dtype=np.int_)
names = []

for line in lines:
  info = line.strip().split(' ')
  n1 = info[0]
  if n1 not in names:
    names.append(n1)
  n2 = info[-1][:-1]
  if n2 not in names:
    names.append(n2)    
  i = names.index(n1)
  j = names.index(n2)
  if info[2] == "gain":
    delta_happiness[i,j] = int(info[3])
  else:
    delta_happiness[i,j] = - int(info[3])

n = len(names)
indexes = np.arange(n)
result = 0

for perm in permutations(indexes[1:]):
  acc = 0
  ns = (indexes[0],) + perm
  for k in range(n):
    i = ns[k]
    j1 = ns[k-1]
    j2 = ns[(k+1)%n]
    acc += delta_happiness[i,j1]
    acc += delta_happiness[i,j2]
  result = max(result, acc)

print(result)
