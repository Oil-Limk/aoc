import sys

import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

lights = np.array([[1 if s == "#" else 0 for s in l.strip()] for l in lines])
mid_lights = np.zeros_like(lights)
(n, m) = mid_lights.shape
steps = 100
lights[n - 1 : 1, m - 1 : 1] = 1

while steps:
    steps -= 1
    for i in range(n):
        for j in range(m):
            x = lights[i, j]
            y = (
                np.sum(
                    lights[max(0, i - 1) : min(n, i + 2), max(0, j - 1) : min(m, j + 2)]
                )
                - x
            )
            mid_lights[i, j] = 1 if y == 3 or (x and y == 2) else 0
    mid_lights[n - 1 : 1, m - 1 : 1] = 1
    if steps:
        steps -= 1
        for i in range(n):
            for j in range(m):
                x = mid_lights[i, j]
                y = (
                    np.sum(
                        mid_lights[
                            max(0, i - 1) : min(n, i + 2), max(0, j - 1) : min(m, j + 2)
                        ]
                    )
                    - x
                )
                lights[i, j] = 1 if y == 3 or (x and y == 2) else 0
        lights[n - 1 : 1, m - 1 : 1] = 1

result = 0

if steps % 2:
    result = np.sum(mid_lights)
else:
    result = np.sum(lights)

print(result)
