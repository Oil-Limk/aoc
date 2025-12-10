import sys

lines = open(sys.argv[1]).readlines()

pos = 50
zeros = 0
max_pos = 100

for rotation in lines:
  letter = rotation[0]
  ammount = int(rotation[1:])
  step = 1
  if letter == "L":
    step = -1
  while ammount:
    pos += step
    pos %= max_pos
    if pos == 0:
      zeros += 1
    ammount -= 1

print(zeros)
