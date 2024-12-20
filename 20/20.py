#! /usr/bin/env python3

import sys
import math
import random
from collections import defaultdict

m = []
Sr, Sc = None, None
Er, Ec = None, None
with open(sys.argv[1], "r") as f_in:
    for r, line in enumerate(f_in):
        m.append([x for x in line.strip()])
        if "S" in line:
            Sr, Sc = r, line.index("S")
        if "E" in line:
            Er, Ec = r, line.index("E")

R = len(m)
C = len(m[0])

def printm(m):
    for line in m:
        print("".join(line))
printm(m)

def inside(r, c):
    return 0<=r<R and 0<=c<C

# Traverse once to find distances
dists = dict()
shortcuts = defaultdict(int)
dist = 0
r, c = Sr, Sc
while True:
    print(r, c)
    dists[(r, c)] = dist
    for jump in range(2, 21):
        for i in range(jump):
            for dr, dc in [(i, jump-i), (-i, -jump+i), (jump-i, -i), (-jump+i, i)]:
                r2, c2 = r+dr, c+dc
                if not inside(r2, c2):
                    continue
                if (r2, c2) in dists:
                    dist2 = dists[(r2, c2)]
                    shortcutlen = dist - dist2 - jump
                    shortcuts[shortcutlen] += 1
    if m[r][c] == "E":
        break
    m[r][c] = "x"
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        r2, c2 = r+dr, c+dc
        if not inside(r2, c2):
            continue
        if m[r2][c2] in ".E":
            r, c = r2, c2
            break
    else:
        raise RuntimeError("pouet")
    dist += 1

ge_100 = 0
print("len #shortcuts")
for shortcutlen in shortcuts:
    nb = shortcuts[shortcutlen]
    print(shortcutlen, nb)
    if shortcutlen >= 100:
        ge_100 += nb

print(ge_100, ">=100")
