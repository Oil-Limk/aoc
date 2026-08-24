import sys

with open(sys.argv[1]) as f:
    raw_instructions = f.read().strip().split("\n")

instructions = [[s.strip(",") for s in r.split(" ")] for r in raw_instructions]

a = 1
b = 0

i = 0

while i < len(instructions):
    instr = instructions[i]
    op = instr[0]
    if op == "hlf":
        if instr[1] == "a":
            a //= 2
        else:
            b //= 2
    elif op == "tpl":
        if instr[1] == "a":
            a *= 3
        else:
            b *= 3
    elif op == "inc":
        if instr[1] == "a":
            a += 1
        else:
            b += 1
    elif op == "jmp":
        i += int(instr[1])
        continue
    elif op == "jie":
        if instr[1] == "a":
            if a % 2 == 0:
                i += int(instr[2])
                continue
        else:
            if b % 2 == 0:
                i += int(instr[2])
                continue
    elif op == "jio":
        if instr[1] == "a":
            if a == 1:
                i += int(instr[2])
                continue
        else:
            if b == 1:
                i += int(instr[2])
                continue
    i += 1

print(b)
