#! /usr/bin/env python3

import sys
from collections import defaultdict

g = []
for line in sys.stdin:
    g.append([c for c in line.strip()])

R = len(g)
C = len(g[0])

def inside(r,c):
    if 0<=r<R and 0<=c<C:
        return True
    return False

seen = [[False for c in range(C)] for r in range(R)]

def fence(r, c, l):
    area = 1
    peri = 0
    seen[r][c] = True
    for r2,c2 in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if not inside(r2,c2):
            peri += 1
        elif l != g[r2][c2]:
            peri += 1
        elif not seen[r2][c2]:
            area2, peri2 = fence(r2, c2, l)
            area += area2
            peri += peri2
    return area, peri

tot = 0
for r in range(R):
    for c in range(C):
        if seen[r][c]:
            continue
        area, peri = fence(r, c, g[r][c])
        tot += area * peri
        print(g[r][c], area, peri, tot)
print(tot)

seen = [[False for c in range(C)] for r in range(R)]
seensides = defaultdict(set)

def followside(r1, c1, l, dr, dc):
    seenother = False
    r, c = r1, c1
    while inside(r, c) \
    and g[r][c] == l \
    and (not inside(r+dr, c+dc) or g[r+dr][c+dc] != l):
        if (dr, dc) in seensides[(r,c)]:
            seenother = True
            break
        seensides[(r,c)].add((dr, dc))
        if dr == 0:
            r += 1
        else:
            c += 1
    r, c = r1, c1
    while inside(r, c) \
    and g[r][c] == l \
    and (not inside(r+dr, c+dc) or g[r+dr][c+dc] != l):
        if (r,c) != (r1,c1) \
        and (dr, dc) in seensides[(r,c)]:
            seenother = True
            break
        seensides[(r,c)].add((dr, dc))
        if dr == 0:
            r -= 1
        else:
            c -= 1
    if seenother:
        return 0
    return 1

def fence2(r, c, l):
    area = 1
    nsides = 0
    seen[r][c] = True
    for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
        r2, c2 = (r+dr,c+dc)
        if not inside(r2,c2) or l != g[r2][c2]:
            nsides += followside(r, c, l, dr, dc)
        elif not seen[r2][c2]:
            area2, nsides2 = fence2(r2, c2, l)
            area += area2
            nsides += nsides2
    return area, nsides

tot = 0
for r in range(R):
    for c in range(C):
        if seen[r][c]:
            continue
        area, nsides = fence2(r, c, g[r][c])
        tot += area * nsides
        print(g[r][c], area, nsides, tot)
print(tot)
