import re
import sys

with open(sys.argv[1]) as f:
    compressed = f.read().strip()


def decompress(comp):
    result = 0
    while True:
        m = re.search("\\(\\d+x\\d+\\)", comp)
        if m is None:
            return result + len(comp)
        a, b = map(int, re.findall("\\d+", m.group()))
        result += m.start() + b * decompress(comp[m.end() : m.end() + a])
        comp = comp[m.end() + a :]


print(decompress(compressed))
