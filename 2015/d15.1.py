import sys
import numpy as np

ingredients = open(sys.argv[1]).readlines()
n = len(ingredients)
ing_mat = np.zeros((n,5), dtype=np.int_)
portion = np.zeros(n, dtype=np.int_)

def ratios(i, top):
  global portion
  if i > -1:
    for m in range(top):
      portion[i] = m
      for _ in ratios(i - 1, top - m):
        yield None
  else:
    yield None

for i, ingredient in enumerate(ingredients):
  for j, prop in enumerate(ingredient.split(':')[-1].strip().split(', ')):
    ing_mat[i,j] = int(prop.split(' ')[-1])

result = 0
for _ in ratios(n - 1, 101):
  mix = portion @ ing_mat
  acc = 1
  for m in mix[:-1]:
    if m < 0:
      acc = 0
      break
    acc *= m
  result = max(result, acc)

print(result)
