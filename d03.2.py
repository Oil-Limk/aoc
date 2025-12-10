import sys

lines = open(sys.argv[1]).read().strip()
banks = lines.split('\n')

result = 0
bpb = 12

for bank in banks:
  nb = bpb
  im = i = 0
  while nb > 0:
    nb -= 1
    bmax = 0
    while i < len(bank) - nb:
      b = int(bank[i])
      if b > bmax:
        bmax = b
        im = i
      i += 1
    result += 10 ** nb * bmax
    i = im + 1

print(result)
