import sys


def str2inttup(rr: str):
    i, j = rr.split("-")
    return int(i), int(j)


with open(sys.argv[1]) as f:
    lines = f.read().strip()
r_ranges, _ = lines.split("\n\n")
ranges = list(map(str2inttup, r_ranges.strip().split("\n")))

a = 0

while a < len(ranges):
    ia, ja = ranges[a]
    b = 0
    merged = False
    while b < len(ranges):
        if b != a:
            ib, jb = ranges[b]
            if ib <= ia <= jb or ib <= ja <= jb:
                ranges[b] = (min(ia, ib), max(ja, jb))
                ranges.pop(a)
                merged = True
                break
        b += 1
    if not merged:
        a += 1

result = 0

for i, j in ranges:
    result += j - i + 1

print(result)
