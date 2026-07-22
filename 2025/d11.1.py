import sys

lines = open(sys.argv[1]).read().strip()

svs:dict[list[str]] = {}
for line in lines.split('\n'):
  k, v = line.split(':')
  svs[k] = v.split()

known_ways:dict[int] = {}

def paths(sv_id:str) -> int:
  if sv_id == "out":
    return 1
  ways = 0
  for n in svs[sv_id]:
    if n not in known_ways:
      known_ways[n] = paths(n)
    ways += known_ways[n]
  return ways

print(paths("you"))
