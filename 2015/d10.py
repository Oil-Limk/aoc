import sys

with open(sys.argv[1]) as f:
    lines = f.read()
seq = lines.strip()


def next_look_and_say(seq):
    next_seq = ""
    n = seq[0]
    c = 1
    for s in seq[1:]:
        if s == n:
            c += 1
        else:
            next_seq += f"{c}{n}"
            n = s
            c = 1
    next_seq += f"{c}{n}"
    return next_seq


for _ in range(50):
    seq = next_look_and_say(seq)

result = len(seq)

print(result)
