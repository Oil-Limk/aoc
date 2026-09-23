import hashlib
import sys

with open(sys.argv[1]) as f:
    door = f.read().strip()

i = 0
result = ["-"] * 8
print("  pwd:", "".join(result), end="\r")
while result.count("-") > 0:
    str_to_hash = f"{door}{i}"
    hash_of_str = hashlib.md5(str_to_hash.encode()).hexdigest()
    if hash_of_str.startswith("00000"):
        index = hash_of_str[5]
        if index.isdigit():
            j = int(index)
            if 0 <= j <= 7 and result[j] == "-":
                result[j] = hash_of_str[6]
                print("  pwd:", "".join(result), end="\r")
    i += 1
print("  pwd:", "".join(result))
