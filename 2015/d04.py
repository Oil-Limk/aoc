import hashlib
import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()

n = 1
s = f"{lines}{n}"

while not hashlib.md5(s.encode()).hexdigest().startswith("000000"):
    n += 1
    s = f"{lines}{n}"
print(n)
