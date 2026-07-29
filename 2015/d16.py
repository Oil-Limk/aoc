import sys

with open(sys.argv[1]) as f:
    lines = f.read().strip()
aunts = lines.split("\n")

real_aunt_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

candidate_sue = ("", 0)  # name, amount of things right

for line in aunts:
    aunt = line.strip()
    i = aunt.find(":")
    number = aunt[:i].split(" ")[1]
    n = 0
    is_candidate = True
    for raw_pair in aunt[i + 1 :].split(","):
        [raw_name, value] = raw_pair.split(":")
        name = raw_name.strip()
        if (
            (name in ("trees", "cats") and real_aunt_sue[name] < int(value))
            or (
                name in ("pomeranians", "goldfish") and real_aunt_sue[name] > int(value)
            )
            or (real_aunt_sue[name] == int(value))
        ):
            n += 1
        else:
            is_candidate = False
            break
    if is_candidate and candidate_sue[1] < n:
        candidate_sue = (number, n)

print(candidate_sue[0])
