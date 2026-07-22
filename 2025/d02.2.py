import sys

line = open(sys.argv[1]).read().strip()
ranges = map(lambda x : x.split('-'), line.split(','))

result = 0

for start, end in ranges:
  for num in range(int(start), int(end) + 1):
    name = str(num)
    l = len(name)
    for di in range(1, (l//2) + 1):
      if not (l % di):
        n1 = name[0:di]
        i = di
        valid = True
        while i < l:
          if not (n1 == name[i:i + di]):
            valid = False
            break
          i += di
        if valid:
          result += num
          break

print(result)
