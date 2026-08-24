import re
import string
import sys

with open(sys.argv[1]) as f:
    old_pwd = f.read().strip()

ls = string.ascii_lowercase


def rule1(pwd):
    return any(pwd[i : i + 3] in ls for i in range(len(pwd) - 2))


def rule2(pwd):
    return not any(s in pwd for s in "oil")


def rule3(pwd):
    return re.fullmatch("\\S*([a-z])\\1\\S*([a-z])\\2\\S*", pwd) is not None


def good_pwd(pwd):
    v1 = rule1(pwd)
    v2 = rule2(pwd)
    v3 = rule3(pwd)
    return v1 and v2 and v3


def next_pwd(pwd):
    l_pwd = list(pwd)
    i = len(l_pwd) - 1
    while i > -1:
        new_i = ls.index(l_pwd[i]) + 1
        l_pwd[i] = ls[new_i % len(ls)]
        if new_i < len(ls):
            break
        i -= 1
    return "".join(l_pwd)


new_pwd = next_pwd(old_pwd)

while not good_pwd(new_pwd):
    new_pwd = next_pwd(new_pwd)

print(new_pwd)
