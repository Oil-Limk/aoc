import sys

reindeers = open(sys.argv[1]).readlines()
RACE_TIME = 2503
winner = 0

for rd in reindeers:
  rd_list = rd.strip().split(' ')
  vel = int(rd_list[3])
  run_time = int(rd_list[6])
  rest_time = int(rd_list[13])
  running_time = (RACE_TIME // (run_time + rest_time)) * run_time + min(RACE_TIME % (run_time + rest_time), run_time)
  distance = running_time * vel
  winner = max(winner, distance)

print(winner)
