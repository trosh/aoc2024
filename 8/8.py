#! /usr/bin/env python3

import sys
from collections import defaultdict

m = []

for line in sys.stdin:
    m.append([c for c in line.strip()])

m1 = []
m2 = []
for line in m:
    print("".join(line))
    m1.append(line[:])
    m2.append(line[:])

R = len(m)
C = len(m[0])

def inside(a):
    if 0<=a[0]<R and 0<=a[1]<C:
        return True
    return False

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
            d  = (y[0]-x[0], y[1]-x[1])
            a1 = (x[0]-d[0], x[1]-d[1])
            a2 = (y[0]+d[0], y[1]+d[1])
            print(x,y,a1,a2)
            if inside(a1):
                m1[a1[0]][a1[1]] = "#"
            if inside(a2):
                m1[a2[0]][a2[1]] = "#"
            xx = x
            while inside(xx):
                m2[xx[0]][xx[1]] = "#"
                xx = (xx[0]-d[0], xx[1]-d[1])
            yy = y
            while inside(yy):
                m2[yy[0]][yy[1]] = "#"
                yy = (yy[0]+d[0], yy[1]+d[1])

nb_antinodes = 0
for line in m1:
    print("".join(line))
    nb_antinodes += sum((1 for c in line if c == "#"))
print(nb_antinodes)

nb_antinodes = 0
for line in m2:
    print("".join(line))
    nb_antinodes += sum((1 for c in line if c == "#"))
print(nb_antinodes)

