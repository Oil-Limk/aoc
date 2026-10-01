import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

values = []
bots = {}

for l in lines:
    ls = l.split(" ")
    if ls[0] == "value":
        values.append((int(ls[-1]), int(ls[1])))
    else:
        bots[int(ls[1])] = {
            "vs": [],
            "bs": (ls[5] == "bot", int(ls[6]), ls[-2] == "bot", int(ls[-1])),
        }

up_next = []

for b, v in values:
    bots[b]["vs"].append(v)
    if len(bots[b]["vs"]) == 2:
        up_next.append(b)

outputs = {}

while up_next:
    bot_num = up_next.pop()
    bots[bot_num]["vs"].sort()
    a, b = bots[bot_num]["vs"]
    b1, n1, b2, n2 = bots[bot_num]["bs"]
    if b1:
        bots[n1]["vs"].append(a)
        if len(bots[n1]["vs"]) == 2:
            up_next.append(n1)
    else:
        outputs[n1] = a
    if b2:
        bots[n2]["vs"].append(b)
        if len(bots[n2]["vs"]) == 2:
            up_next.append(n2)
    else:
        outputs[n2] = b

result = outputs[0] * outputs[1] * outputs[2]

print(result)
