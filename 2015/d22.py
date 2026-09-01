import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

boss_hp = int(lines[0].split(' ')[-1])
boss_damage = int(lines[1].split(' ')[-1])

player_hp = 50
player_mana = 500

(cost, damage, armor, heal, mana, turns)



magic_missile = (4, 0, 0, 0, 1)
drain =         (2, 0, 2, 0, 1)
shield =        (0, 7, 0, 0, 6)
poison =        (3, 0, 0, 0, 6)
recharge =      (0, 0, 0, 101, 5)

def magic_missile(p_hp, p_m, p_d, p_a, b_hp, b_d):
    return p_hp, p_m, p_d, p_a, b_hp - 4, b_d

def drain(p_hp, p_m, p_d, p_a, b_hp, b_d):
    return p_hp + 2, p_m, p_d, p_a, b_hp - 2, b_d

def shield(p_hp, p_m, p_d, p_a, b_hp, b_d):
    return p_hp, p_m, p_d, p_a + 7, b_hp, b_d

def player_turn(p_hp, p_m, p_d, p_a, b_hp, b_d):
    if b_hp <= 0:
        return (True, 0)
    if p_hp <= 0:
        return (False, 0)

    # effects
    for i in range(len(effects)):
        if effects[i][0] == "poison":
            b_hp -= 3
            effects[i][1] -= 1
        elif effects[i][0] == "shield":
            p_a += 7
            effects[i][1] -= 1
        elif effects[i][0] == "recharge":
            p_m += 101
            effects[i][1] -= 1

        if b_hp <= 0:
            return (True, 0)
        if p_hp <= 0:
            return (False, 0)
    
    # cast

    1, 53, magic_missile
    1, 73, drain
    6, 133, shield
    6, 173, poison
    5, 229, recharge
    
    player_turn(p_ph - max(1, b_d - p_a), p_m, p_d, p_a, b_hp, b_d)

def boss_turn(p_hp, p_m, p_d, p_a, b_hp, b_d):
    if b_hp <= 0:
        return (True, 0)
    if p_hp <= 0:
        return (False, 0)

    # effects

    if b_hp <= 0:
        return (True, 0)
    if p_hp <= 0:
        return (False, 0)

    # hit
    
