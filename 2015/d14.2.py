import sys
import numpy as np

reindeers = open(sys.argv[1]).readlines()
RACE_TIME = 2503

n = len(reindeers)

velocity = np.zeros(n, dtype=np.int_)
run_time = np.zeros_like(velocity)
rest_time = np.zeros_like(velocity)
distance = np.zeros_like(velocity)
running_at = np.zeros_like(velocity)
count_downs = np.zeros_like(velocity)
points = np.zeros_like(velocity)

for i, rd in enumerate(reindeers):
  rd_list = rd.strip().split(' ')
  velocity[i] = int(rd_list[3])
  run_time[i] = int(rd_list[6])
  rest_time[i] = int(rd_list[13])

sec = 0
while sec < RACE_TIME:
  out_of_t = (count_downs == 0)
  if np.any(out_of_t):
    running_at ^= np.where(out_of_t, velocity, 0)
    count_downs += np.where(out_of_t, np.where(running_at == 0, rest_time, run_time), 0)
  distance += running_at
  count_downs -= 1
  points += np.where(distance == max(distance), 1, 0)
  sec += 1

winner = max(points)

print(winner)
