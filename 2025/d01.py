import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()

pos = 50
zeros = 0
max_pos = 100

for rotation in lines:
    letter = rotation[0]
    amount = int(rotation[1:])
    step = 1
    if letter == "L":
        step = -1
    while amount:
        pos += step
        pos %= max_pos
        if pos == 0:
            zeros += 1
        amount -= 1

print(zeros)
