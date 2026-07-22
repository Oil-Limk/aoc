import sys

aunts = open(sys.argv[1]).readlines()

real_aunt_sue = {
  "children"    : 3,
  "cats"        : 7,
  "samoyeds"    : 2,
  "pomeranians" : 3,
  "akitas"      : 0,
  "vizslas"     : 0,
  "goldfish"    : 5,
  "trees"       : 3,
  "cars"        : 2,
  "perfumes"    : 1,
}

candidate_sue = ("", 0) # name, amount of things right

for line in aunts:
  aunt = line.strip()
  i = aunt.find(':')
  number = aunt[:i].split(' ')[1]
  n = 0
  is_candidate = True
  for raw_pair in aunt[i+1:].split(','):
    [raw_name, value] = raw_pair.split(":")
    name = raw_name.strip()
    if name in ("trees", "cats"):
      if real_aunt_sue[name] < int(value):
        n += 1
    elif name in ("pomeranians", "goldfish"):
      if real_aunt_sue[name] > int(value):
        n += 1
    elif real_aunt_sue[name] == int(value):
      n += 1
    else:
      is_candidate = False
      break
  if is_candidate:
    if candidate_sue[1] < n:
      candidate_sue = (number, n)
  
print(candidate_sue[0])
