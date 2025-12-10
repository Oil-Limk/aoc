import sys

lines = open(sys.argv[1]).readlines()

pos = 50
zeros = 0
max_pos = 100

for rotation in lines:
  letter = rotation[0]
  ammount = int(rotation[1:])
  if letter == "L":
    pos -= ammount
  else:
    pos += ammount
  pos %= 100
  if pos == 0:
    zeros += 1

print(zeros)
