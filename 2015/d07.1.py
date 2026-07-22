import sys

booklet = open(sys.argv[1]).readlines()
circuit = {}
for raw_inst in booklet:
  inst_list = raw_inst.strip().split(' ')
  n = len(inst_list)
  name = inst_list[-1]
  if n == 3:
    circuit[name] = ("VAL", inst_list[0], None)
  elif n == 4:
    circuit[name] = (inst_list[0], inst_list[1], None)
  elif n == 5:
    circuit[name] = (inst_list[1], inst_list[0], inst_list[2])

NOT_MASK = 65535

def emulate(wire):
  if str(wire).isdecimal():
    return int(wire)
  else:
    op, v1, v2 = circuit[wire]
    if op == "VAL":
      val = emulate(v1)
    if op == "NOT":
      val = emulate(v1) ^ NOT_MASK
    if op == "AND":
      val = emulate(v1) & emulate(v2)
    if op == "OR":
      val = emulate(v1) | emulate(v2)
    if op == "RSHIFT":
      val = emulate(v1) >> emulate(v2)
    if op == "LSHIFT":
      val = emulate(v1) << emulate(v2)
    circuit[wire] = ("VAL", val, None)
    return val

print(emulate("a"))
