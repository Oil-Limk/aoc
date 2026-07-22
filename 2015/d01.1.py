import sys

floor = open(sys.argv[1]).readline().strip()

print(floor.count('(') - floor.count(')'))
