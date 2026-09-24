import re
import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

result = 0
regex = "(\\w)(?!\\1)(\\w)\\1\\w*(\\[.*)*\\[\\w*\\2\\1\\2|\\[\\w*(\\w)(?!\\4)(\\w)\\4.*\\]\\w*\\5\\4\\5"

for l in lines:
    if re.search(regex, l) is not None:
        result += 1

print(result)
