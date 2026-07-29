import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()
dig_list = lines.split("\n")
escaped = {"\\\\": 1, '\\"': 1, "\\x": 3}
result = 2 * len(dig_list)
for s in dig_list:
    result += s.count('"')
    result += s.count("\\")

print(result)
