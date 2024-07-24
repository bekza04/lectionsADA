import sys

fname = sys.argv[1]

with open(fname, 'r') as f:
    l = f.read().splitlines()
print(l)
