import sys
from itertools import combinations

import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().strip()
raw_machines = [l.split(" ")[1:] for l in lines.split("\n")]


def machines(rms):
    for rm in rms:
        target = np.array([int(x) for x in rm.pop()[1:-1].split(",")])
        buttons = []
        for b in rm:
            ba = np.zeros_like(target)
            for i in b[1:-1].split(","):
                ba[int(i)] = 1
            buttons.append(ba)
        yield buttons, target


def button_comb(bs):
    for bl in range(len(bs) + 1):
        for bc in combinations(bs, bl):
            yield bc, bl


def search(bs, t, inf):
    if np.all(t == 0):
        return 0
    if np.any(t < 0):
        return inf
    name = "".join(str(b) for b in bs) + str(t)
    try:
        return but_tar_cache[name]
    except KeyError:
        sol = inf
        try:
            for sum_acc, bl in lights_cache[str(t % 2)]:
                sol = min(sol, 2 * search(bs, (t - sum_acc) // 2, inf) + bl)
        except KeyError:
            pass
        but_tar_cache[name] = sol
        return sol


result = 0
but_tar_cache = {}
for buttons, target in machines(raw_machines):
    lights_cache = {}
    for bc, bl in button_comb(buttons):
        par_acc = np.zeros_like(target)
        sum_acc = np.zeros_like(target)
        for b in bc:
            par_acc ^= b
            sum_acc += b
        try:
            lights_cache[str(par_acc)].append((sum_acc, bl))
        except KeyError:
            lights_cache[str(par_acc)] = [(sum_acc, bl)]

    but_tar_cache = {}
    result += search(buttons, target, sum(target))

print(result)
