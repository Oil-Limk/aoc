import sys

import numpy as np

with open(sys.argv[1]) as f:
    lines = f.read().strip()
presents_and_areas = lines.split("\n")
raw_presents = presents_and_areas[:30]
raw_areas = presents_and_areas[30:]
presents = []
areas = []

p = None
i = 0
for sp in raw_presents:
    sp = sp.strip()
    if sp:
        if sp[0].isdecimal():
            p = np.zeros((3, 3), dtype=np.int_)
            continue
        for j, s in enumerate(sp):
            if s == "#":
                p[i, j] = 1
        i += 1
    if i == 3:
        tiles = [p.copy()]
        for _ in range(3):
            p = np.rot90(p)
            tiles.append(p.copy())
        presents.append(tiles)
        i = 0

cache = {}


def u_can_tile(a, b, ps):
    # use presents
    area = np.zeros((a, b), dtype=np.int_)

    def tetris(pns):
        name = str(area) + str(ps)
        if name in cache:
            return cache[name]

        if sum(pns) == 0:
            return True

        for i in range(len(pns)):
            if pns[i] == 0:
                continue
            pns[i] -= 1
            for piece in presents[i]:
                for col in range(b-2):
                    for row in range(a-2):
                        if np.any(area[row:row+3,col:col+3] & piece):
                            continue
                        area[row:row+3,col:col+3] ^= piece
                        if tetris(pns.copy()):
                            print("done")
                            return True
                        area[row:row+3,col:col+3] ^= piece
                        break
            pns[i] += 1

        cache[name] = False
        return False

    u_can = tetris(ps)
    cache[str(area) + str(ps)] = u_can
    return u_can


result = 0
for sa in raw_areas:
    axb, ps = sa.strip().split(": ")
    a, b = axb.split("x")
    if u_can_tile(int(a), int(b), [int(n) for n in ps.split(" ")]):
        result += 1


print(result)
