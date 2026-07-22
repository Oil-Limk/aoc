import sys

dig_list = open(sys.argv[1]).readlines()
escaped = { "\\\\" : 1, "\\\"" : 1, "\\x" : 3 }
result = 2 * len(dig_list)
for s in dig_list:
  result += s.count('"')
  result += s.count('\\')

print(result)
