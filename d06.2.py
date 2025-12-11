import sys

lines = open(sys.argv[1]).read().strip("\n")
worksheet = lines.split('\n')
m = len(worksheet)
n = len(worksheet[0])

result = 0

j = 0
acc = 0
op = ""
while j < n:
  snum = ""
  i = 0
  while i < m:
    s = worksheet[i][j]
    if s.isdigit():
      snum += s
    elif s != ' ':
      op = s
    i += 1
  j += 1
  if not snum:
    result += acc
    acc = 0
    op = ""
    continue
  if not acc:
    acc = int(snum)
  elif op == '+':
    acc += int(snum)
  else:
    acc *= int(snum)
  if j == n:
    result += acc

print(result)
