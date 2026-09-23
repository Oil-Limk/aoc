import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

result = "Ready to code!"

print(result)
