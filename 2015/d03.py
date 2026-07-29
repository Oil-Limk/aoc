import sys

import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().strip()

direction = {
    "^": np.array([0, 1]),
    "v": np.array([0, -1]),
    ">": np.array([1, 0]),
    "<": np.array([-1, 0]),
}

house = np.zeros(2)
houses = set()
houses.add(str(house))

for d in lines[::2]:
    house += direction[d]
    houses.add(str(house))

house = np.zeros(2)

for d in lines[1::2]:
    house += direction[d]
    houses.add(str(house))

print(len(houses))
