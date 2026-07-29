import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()

message = lines.split(" ")
col = int(message[-1][:-1]) - 1
both = col + int(message[-3][:-1]) - 1
exponent = col + (both * (both + 1)) // 2
start = 20151125
factor = 252533
module = 33554393
result = start * pow(factor, exponent, module) % module
print(result)
