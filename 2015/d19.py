import re
import sys

with open(sys.argv[1]) as f:
    _, molecule = f.read().strip().split("\n\n")

molecule = molecule.replace("Rn", "(")
molecule = molecule.replace("Ar", ")")
molecule = molecule.replace("Y", ",")
molecule = re.sub("[a-z]", "", molecule)
molecule = re.sub("[A-Z]", "X", molecule)

n = 0
while len(molecule) > 1:
    for p in ["X(X,X,X)", "X(X,X)", "X(X)", "XX"]:
        if p in molecule:
            molecule = molecule.replace(p, "X", 1)
            n += 1
print(n, molecule)
