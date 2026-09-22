import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

x, y = 0, 2

keypad = [
    "  1  ",
    " 234 ",
    "56789",
    " ABC ",
    "  D  ",
]

for line in lines:
    for s in line:
        if s == "U":
            y -= 1
            y = max(abs(x - 2), y)
        elif s == "D":
            y += 1
            y = min(4 - abs(x - 2), y)
        elif s == "L":
            x -= 1
            x = max(abs(y - 2), x)
        else:
            x += 1
            x = min(4 - abs(y - 2), x)
    print(keypad[y][x], end="")
print()
