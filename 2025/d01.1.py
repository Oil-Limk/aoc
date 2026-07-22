import sys

lines = open(sys.argv[1]).readlines()

pos = 50
zeros = 0
max_pos = 100

for rotation in lines:
  letter = rotation[0]
  amount = int(rotation[1:])
  if letter == "L":
    pos -= amount
  else:
    pos += amount
  pos %= 100
  if pos == 0:
    zeros += 1

print(zeros)
