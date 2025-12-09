import sys

lines = open(sys.argv[1]).read().strip()
banks = lines.split('\n')

result = 0

for bank in banks:
  bs = list(map(lambda x : int(x), bank))
  bmax = im = i = 0
  while i < len(bs) - 1:
    b = bs[i]
    if b > bmax:
      bmax = b
      im = i
    i += 1
  result += 10 * bmax + max(bs[im+1:])

print(result)
