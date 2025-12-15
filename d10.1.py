import sys

lines = open(sys.argv[1]).read().strip()
raw_machines = list(map(lambda x : x.split(' '), lines.split('\n')))

machines = []
max_len_b = 0

for rm in raw_machines:
  rm.pop()
  lights = rm.pop(0)[1:-1][::-1]
  target = 0
  for l in lights:
    target *= 2
    target += 1 if l == '#' else 0
  buttons = []
  for b in rm:
    hits = 0
    for l in b[1:-1].split(','):
      hits += 2 ** int(l)
    buttons.append(hits)
  ll = len(rm)
  if ll > max_len_b:
    max_len_b = ll
  machines.append((target, buttons, ll))

pos_sol = []

for i in range(2 ** max_len_b):
  bi = bin(i)[2:]
  pos_sol.append((bi, bi.count('1')))

pos_sol.sort(key=lambda x : x[-1])

result = 0

for target, buttons, lb in machines:
  for sol, ones in pos_sol:
    l = min(len(sol), lb)
    acc = 0
    for i in range(1, l+1):
      acc ^= buttons[-i] if sol[-i] == '1' else 0
    if acc == target:
      result += ones
      break

print(result)
