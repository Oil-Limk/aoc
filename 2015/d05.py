import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()
strings = lines.split("\n")

result = 0
for s in strings:
    s = s.strip()
    pair = False
    letter = False
    for i in range(len(s) - 2):
        seg = s[i : i + 2]
        rest = s[i + 2 :]
        if seg in rest:
            pair = True
        if seg[0] == rest[0]:
            letter = True
        if letter and pair:
            result += 1
            break

print(result)
