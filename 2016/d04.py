import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

result = 0


def rotate(s, n):
    return "".join(
        " " if x == "-" else chr(ord("a") + ((ord(x) + n - ord("a")) % 26)) for x in s
    )


for l in lines:
    checksum = l[-6:-1]
    real_name = l[:-10]
    name = real_name.replace("-", "")
    real_cs = []
    for s in name:
        if s in real_cs:
            continue
        real_cs.append(s)
    real_cs.sort()
    real_cs.sort(key=lambda x: name.count(x), reverse=True)
    if checksum == "".join(real_cs[:5]):
        room_id = int(l[-10:-7])
        decrypt_name = rotate(real_name, room_id)
        if decrypt_name.find("north") != -1:
            print(room_id, decrypt_name)
