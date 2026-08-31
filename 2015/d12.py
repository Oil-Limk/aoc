import sys

with open(sys.argv[1]) as f:
    json_str = f.read().strip()

pile = []
i = 0
s = ""
n = 0
banned = (False, len(pile))
while i < len(json_str):
    if json_str[i] in "-0123456789":
        s += json_str[i]
    elif s:
        n += int(s)
        s = ""
    if json_str[i] == "{":
        pile.append(n)
        n = 0
    elif json_str[i] == "}":
        if banned[0]:
            if banned[1] == len(pile):
                banned = (False, len(pile))
            n = pile.pop()
        else:
            n += pile.pop()
    elif not banned[0] and json_str[i : i + 6] == ':"red"':
        banned = (True, len(pile))
    i += 1

print(n)
