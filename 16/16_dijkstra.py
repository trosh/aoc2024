#! /usr/bin/env python3

import sys
import math
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
        print("".join(line), end="")
    print()
printm(m)

ids = {
        (-1, 0) : 0,
        (+1, 0) : 1,
        (0, -1) : 2,
        (0, +1) : 3,
        }
def dirid(dr, dc):
    return ids[(dr,dc)]

def nodeid(u):
    r, c, dr, dc = u
    return 4 * (r * C + c) + dirid(dr, dc)

def inside(r, c):
    return 0<=r<R and 0<=c<C

cost = [None] * (R * C * 4)
prev = dict()
unvisited = list()
for r in range(R):
    for c in range(C):
        if m[r][c] == "#":
            continue
        for dr, dc in ids:
            u = (r, c, dr, dc)
            cost[nodeid(u)] = math.inf
            unvisited.append(u)
u = (Sr,Sc,0,1)
cur = [u]
unvisited.remove(u)
cost[nodeid(u)] = 0
niter = 0
print("\033[2J\033[7m", end="")
while cur != []:
    u_i = 0
    u = cur[u_i]
    mincost = cost[nodeid(u)]
    for i in range(1, len(cur)):
        u2 = cur[i]
        thiscost = cost[nodeid(u2)]
        if mincost > thiscost:
            mincost = thiscost
            u = u2
            u_i = i
    del cur[u_i]
    r,c,dr,dc = u
    print(f"\033[{r+1};{2*c+1}H  ", end="")
    if niter % 10 == 0:
        sys.stdout.flush()
    frwd = dr + dc*1j
    left = frwd * 1j
    rght = frwd * -1j
    lr, lc = int(left.real), int(left.imag)
    rr, rc = int(rght.real), int(rght.imag)
    neighbours = [
            (r+dr, c+dc, dr, dc, 1),
            (r, c, lr, lc, 1000),
            (r, c, rr, rc, 1000),
        ]
    for neighbour in neighbours:
        r, c, dr, dc, extracost = neighbour
        v = (r, c, dr, dc)
        if not inside(r, c):
            continue
        incur = v in cur
        inunv = v in unvisited
        assert not (incur and inunv)
        if not incur and not inunv:
            continue
        alt = mincost + extracost
        vid = nodeid(v)
        if cost[vid] == alt:
            prev[vid].append(u)
        if cost[vid] > alt:
            cost[vid] = alt
            prev[vid] = [u]
            if inunv:
                unvisited.remove(v)
                cur.append(v)
    niter += 1
print("\033[31m", end="")

mincost = math.inf
for dr, dc in ids:
    v = (Er, Ec, dr, dc)
    c = cost[nodeid(v)]
    #print(v, c)
    if mincost > c:
        mincost = c
        u = v
ntiles_on_best_paths = 0
seen = [[False] * C for _ in range(R)]
todo = [u]
while todo != []:
    cur = todo
    todo = []
    for u in cur:
        r, c, dr, dc = u
        if not seen[r][c]:
            seen[r][c] = True
            ntiles_on_best_paths += 1
        print(f"\033[{r+1};{2*c+1}H  ", end="")
        sys.stdout.flush()
        uid = nodeid(u)
        if uid not in prev:
            continue
        for v in prev[uid]:
            todo.append(v)
print(f"\033[m\033[{R+1};1H")
print("mincost:", mincost)
print("nb tiles on best paths:", ntiles_on_best_paths)
