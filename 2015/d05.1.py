import sys

strings = open(sys.argv[1]).readlines()
naughty_pairs = {"ab", "cd", "pq", "xy"}
vowels = "aeiou"

result = len(strings)
for s in strings:
  s = s.strip()
  naughty = False
  pair = False
  vow = 0
  for i in range(len(s)):
    seg = s[i:i+2]
    if seg in naughty_pairs:
      naughty = True
      break
    if not pair and seg.count(seg[0]) == 2:
      pair = True
    if vow < 3 and seg[0] in vowels:
      vow += 1
  if naughty or vow < 3 or not pair:
    result -= 1
print(result)
