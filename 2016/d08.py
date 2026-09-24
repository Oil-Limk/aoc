import re
import sys

import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

screen = np.zeros((6, 50))


def rect(w, t):
    screen[:t, :w] = 1


def rotate_row(y, n):
    buff = screen[y, :].copy()
    m = buff.size
    for i in range(m):
        screen[y, (n + i) % m] = buff[i]


def rotate_col(x, n):
    buff = screen[:, x].copy()
    m = buff.size
    for i in range(m):
        screen[(n + i) % m, x] = buff[i]


for l in lines:
    a, b = map(int, re.findall("\\d+", l))
    if l[1] == "e":
        rect(a, b)
    elif l[7] == "r":
        rotate_row(a, b)
    else:
        rotate_col(a, b)

for i in range(6):
    for j in range(50):
        print("#" if screen[i, j] else " ", end="")
    print()
