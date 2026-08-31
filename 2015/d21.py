import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

boss_hit_points = int(lines[0].split(' ')[-1])
boss_damage = int(lines[1].split(' ')[-1])
boss_armor = int(lines[2].split(' ')[-1])

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]
armors = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]
rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]
player_hit_points = 100
max_gold = 0
for w in weapons:
    for a in armors:
        for r1, r2 in combinations(rings, 2):
            gold = w[0] + a[0] + r1[0] + r2[0]
            player_damage = w[1] + r1[1] + r2[1]
            player_armor = a[2] + r1[2] + r2[2]
            boss_attack = max(1, boss_damage - player_armor)
            player_attack = max(1, player_damage - boss_armor)
            boss_turns = (boss_hit_points + player_attack - 1) // player_attack
            player_turns = (player_hit_points + boss_attack - 1) // boss_attack
            if player_turns < boss_turns:
                max_gold = max(max_gold, gold)

print(max_gold)
