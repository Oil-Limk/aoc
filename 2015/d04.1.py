import sys
import hashlib

code = open(sys.argv[1]).readline().strip()
n = 1
s = f"{code}{n}"

while not hashlib.md5(s.encode()).hexdigest().startswith("00000"):
  n += 1
  s = f"{code}{n}"
print(n)
