import sys

lines = open(sys.argv[1]).read().strip()
banks = lines.split('\n')

result = 0

for bank in banks:
  bmax = im = i = 0
  while i < len(bank) - 1:
    b = int(bank[i])
    if b > bmax:
      bmax = b
      im = i
    i += 1
  result += 10 * bmax + int(max(bank[im+1:]))

print(result)
