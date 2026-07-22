import sys
import numpy as np

raw_insts = open(sys.argv[1]).readlines()

grid = np.zeros((1000,1000), dtype=np.int_)
for raw_inst in raw_insts:
  parts = raw_inst.strip().split(',')
  p1 = parts[0].split(' ')[-2:]
  inst = p1[0]
  x1 = int(p1[1])
  y1 = int(parts[1].split(' ')[0])
  x2 = int(parts[1].split(' ')[-1]) + 1
  y2 = int(parts[2].split(' ')[0]) + 1
  if inst == "on": 
    grid[x1:x2,y1:y2] = 1
  elif inst == "off": 
    grid[x1:x2,y1:y2] = 0
  elif inst == "toggle": 
    grid[x1:x2,y1:y2] ^= 1

print(sum(sum(grid)))
