import sys

lines = open(sys.argv[1]).read().strip()
rworksheet = lines.split('\n')
lrw = len(rworksheet)
worksheet = []

i = 0
while i < lrw:
  lw = rworksheet[i].split(' ')
  j = 0
  while j < len(lw):
    if lw[j]:
      if i < lrw - 1:
        lw[j] = int(lw[j])
      j += 1
    else:
      lw.pop(j)
  worksheet.append(lw)
  i += 1

ops = worksheet.pop()
result_row = worksheet.pop(0)
n = len(ops)
i = 0

while i < len(worksheet):
  row = worksheet[i]
  j = 0
  while j < n:
    if ops[j] == '+':
      result_row[j] += row[j]
    else:
      result_row[j] *= row[j]
    j += 1
  i += 1

result = sum(result_row)

print(result)
