import sys
import numpy as np

line = open(sys.argv[1]).readline()

direction = {
  "^" : np.array([0,1]),
  "v" : np.array([0,-1]),
  ">" : np.array([1,0]),
  "<" : np.array([-1,0]),
}

house = np.zeros(2)
houses = set()
houses.add(str(house))

for d in line[::2]:
  house += direction[d]
  houses.add(str(house))

house = np.zeros(2)

for d in line[1::2]:
  house += direction[d]
  houses.add(str(house))

print(len(houses))
