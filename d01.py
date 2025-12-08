import sys

input = open(sys.argv[1]).read().rstrip()
lines = input.split("\n")

pos = 50
ceros = 0
total_positions = 100

for rotation in lines:
    letter = rotation[0]
    ammount = int(rotation[1:])
    if letter == "L":
        pos -= ammount
    else:
        pos += ammount
    pos %= 100
    if pos == 0:
        ceros += 1

print(ceros)

