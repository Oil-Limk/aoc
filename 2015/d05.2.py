import sys

strings = open(sys.argv[1]).readlines()

result = 0
for s in strings:
  s = s.strip()
  pair = False
  lett = False
  for i in range(len(s) - 2):
    seg = s[i:i+2]
    rest = s[i+2:]
    if seg in rest:
      pair = True
    if seg[0] == rest[0]:
      lett = True
    if lett and pair:
      result += 1
      break

print(result)
