#! /usr/bin/env python3

import sys

g = []
for line in sys.stdin:
    g.append([c for c in line.strip()])

R = len(g)
C = len(g[0])

seen = [[False for c in range(C)] for r in range(R)]

def inside(r,c):
    if 0<=r<R and 0<=c<C:
        return True
    return False

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
