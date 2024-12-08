#! /usr/bin/env python3

import sys
from collections import defaultdict

m = []

for line in sys.stdin:
    m.append([c for c in line.strip()])

for line in m:
    print("".join(line))

R=len(m)
C=len(m[0])

ants = defaultdict(list)
for r in range(R):
    for c in range(C):
        if m[r][c] != ".":
            ants[m[r][c]].append((r,c))

for k in ants:
    print(k)
    for x in ants[k]:
        for y in ants[k]:
            if x==y: continue
            d = (x[0]-y[0],x[1]-y[1])
            a1 = (y[0]-d[0],y[1]-d[1])
            a2 = (x[0]+d[0],x[1]+d[1])
            print(x,y,a1,a2)
            if 0<=a1[0]<R and 0<=a1[1]<C:
                m[a1[0]][a1[1]]="#"
            if 0<=a2[0]<R and 0<=a2[1]<C:
                m[a2[0]][a2[1]]="#"

nb_antinodes=0
for line in m:
    print("".join(line))
    nb_antinodes += sum((1 for c in line if c == "#"))
print(nb_antinodes)

