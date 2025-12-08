import sys

line = open(sys.argv[1]).read().strip()
ranges = map(lambda x : x.split('-'), line.split(','))

result = 0

for start, end in ranges:
    for i in range(int(start), int(end) + 1):
        si = str(i)
        l = len(si)//2
        if si[l:] == si[:l]:
            result += int(i)

print(result)
