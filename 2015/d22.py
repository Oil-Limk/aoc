import sys

from numpy import inf

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")


# EFFECTS
def up_armor(armor, b_hp, p_mana):
    return (armor + 7, b_hp, p_mana)


def hit_b(armor, b_hp, p_mana):
    return (armor, b_hp - 3, p_mana)


def up_mana(armor, b_hp, p_mana):
    return (armor, b_hp, p_mana + 101)


# SPELLS
def magic_missile(p_hp, b_hp, uac, hbc, umc):
    return p_hp, b_hp - 4, uac, hbc, umc, True


def drain(p_hp, b_hp, uac, hbc, umc):
    return p_hp + 2, b_hp - 2, uac, hbc, umc, True


def shield(p_hp, b_hp, uac, hbc, umc):
    if uac == 0:
        return p_hp, b_hp, 6, hbc, umc, True
    else:
        return p_hp, b_hp, uac, hbc, umc, False


def poison(p_hp, b_hp, uac, hbc, umc):
    if hbc == 0:
        return p_hp, b_hp, uac, 6, umc, True
    else:
        return p_hp, b_hp, uac, hbc, umc, False


def recharge(p_hp, b_hp, uac, hbc, umc):
    if umc == 0:
        return p_hp, b_hp, uac, hbc, 5, True
    else:
        return p_hp, b_hp, uac, hbc, umc, False


spells = {53: magic_missile, 73: drain, 113: shield, 173: poison, 229: recharge}
result = inf


def game(p_hp, p_mana, b_hp, b_damage, used_mana, uac, hbc, umc):
    # cache
    global result
    if result < used_mana:
        return

    # check
    if b_hp <= 0:
        result = min(result, used_mana)
        return

    # reset player armor
    armor = 0

    # effects
    if uac > 0:
        armor, b_hp, p_mana = up_armor(armor, b_hp, p_mana)
        uac -= 1
    if hbc > 0:
        armor, b_hp, p_mana = hit_b(armor, b_hp, p_mana)
        hbc -= 1
    if umc > 0:
        armor, b_hp, p_mana = up_mana(armor, b_hp, p_mana)
        umc -= 1

    # check
    if b_hp <= 0:
        result = min(result, used_mana)
        return

    # boss deals damage
    p_hp -= max(1, b_damage - armor)

    # check
    if p_hp <= 0:
        return

    # hard
    p_hp -= 1
    if p_hp <= 0:
        return

    # reset player armor
    armor = 0

    # effects
    if uac > 0:
        armor, b_hp, p_mana = up_armor(armor, b_hp, p_mana)
        uac -= 1
    if hbc > 0:
        armor, b_hp, p_mana = hit_b(armor, b_hp, p_mana)
        hbc -= 1
    if umc > 0:
        armor, b_hp, p_mana = up_mana(armor, b_hp, p_mana)
        umc -= 1

    # check
    if b_hp <= 0:
        result = min(result, used_mana)
        return

    # player casts spell
    for price, spell in spells.items():
        if price <= p_mana:
            new_p_hp, new_b_hp, new_uac, new_hbc, new_umc, worked = spell(
                p_hp, b_hp, uac, hbc, umc
            )
            if worked:
                game(
                    new_p_hp,
                    p_mana - price,
                    new_b_hp,
                    b_damage,
                    used_mana + price,
                    new_uac,
                    new_hbc,
                    new_umc,
                )


def start_game(p_hp, p_mana, b_hp, b_damage):
    # hard
    p_hp -= 1
    if p_hp <= 0:
        return

    # player casts spells
    for price, spell in spells.items():
        if price <= p_mana:
            new_p_hp, new_b_hp, new_uac, new_hbc, new_umc, worked = spell(
                p_hp, b_hp, 0, 0, 0
            )
            if worked:
                game(
                    new_p_hp,
                    p_mana - price,
                    new_b_hp,
                    b_damage,
                    price,
                    new_uac,
                    new_hbc,
                    new_umc,
                )


start_game(
    p_hp=50,
    p_mana=500,
    b_hp=int(lines[0].split(" ")[-1]),
    b_damage=int(lines[1].split(" ")[-1]),
)

print(result)
