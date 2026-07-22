import sys

floor = open(sys.argv[1]).readline().strip()

n = 0
p = 0
for i in floor:
  p += 1
  if i == '(':
    n += 1
  else:
    n -= 1
  if n < 0:
    break
print(p)
