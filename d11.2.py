import sys

lines = open(sys.argv[1]).read().strip()

svs:dict[list[str]] = {}
for line in lines.split('\n'):
  k, v = line.split(':')
  svs[k] = v.split()

def paths_to_goal(start:str, goal:str) -> int:
  
  known_ways:dict[int] = {}

  def paths(sv_id:str) -> int:
    if sv_id == goal:
      return 1
    ways = 0
    try:
      for n in svs[sv_id]:
        if n not in known_ways:
          known_ways[n] = paths(n)
        ways += known_ways[n]
      return ways
    except:
      return 0
  return paths(start)

svr2fft = paths_to_goal("svr", "fft")
fft2dac = paths_to_goal("fft", "dac")
dac2out = paths_to_goal("dac", "out")

result = svr2fft * fft2dac * dac2out

print(result)
