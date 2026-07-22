import sys

dig_list = open(sys.argv[1]).readlines()
escaped = { "\\\\" : 1, "\\\"" : 1, "\\x" : 3 }
result = 2 * len(dig_list)
for s in dig_list:
  s = s[1:-2]
  i = 0
  while i < len(s):
    seg = s[i:i+2]
    if seg in escaped:
      result += escaped[seg]
      i += 1
    i += 1

print(result)
