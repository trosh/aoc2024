#! /usr/bin/env python3

import sys
import math
import random

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

def printm(m):
    for line in m:
        print("".join(line), end="")
printm(m)

#def dfs(m, r, c, dr, dc):
#    if m[r][c] == "E":
#        printm(m)
#        return 0
#    prev = m[r][c]
#    m[r][c] = "☺"
#    mincost = math.inf
#    r2, c2 = r+dr, c+dc
#    if m[r2][c2] in ".E":
#        #print(r, c, "+", dr, dc, "=", r2, c2, m[r2][c2])
#        cost = 1 + dfs(m, r2, c2, dr, dc)
#        if mincost > cost:
#            mincost = cost
#    cplx = dr + dc*1j
#    for rot in [1j, -1j]: # Left, Right
#        turn = cplx * rot
#        tr, tc = int(turn.real), int(turn.imag)
#        r2 = r + tr
#        c2 = c + tc
#        if m[r2][c2] in ".E":
#            #print(r, c, "+", tr, tc, "=", r2, c2, m[r2][c2])
#            cost = 1001 + dfs(m, r2, c2, tr, tc)
#            if mincost > cost:
#                mincost = cost
#    m[r][c] = prev
#    return mincost

def printp(positions, cost):
    print("\033[2J\033[7m", end="")
    for r, c in positions:
        print(f"\033[{r+1};{2*c+1}H  ", end="")
    print(f"\033[1;1H\033[m{cost}")

def debug_signal_handler(signal, frame):
    import pdb
    pdb.set_trace()
import signal
signal.signal(signal.SIGINT, debug_signal_handler)

def dfs(m):
    minlen = []
    for line in m:
        minlen.append([math.inf for _ in line])
    positions = [(Sr,Sc)] # "S"
    directions = [(0,1)] # East
    turns = [0]
    costs = [0]
    cost = 0
    mincost = math.inf
    nbpaths = 0
    step = 0
    backtrack = False
    while positions != []:
        step += 1
        if step > 20000:
            printp(positions, mincost)
            step = 0
        #if backtrack:
        #    print("backtrack")
        #print(positions)
        #print(directions)
        #print(turns)
        #print(costs)
        last = len(positions) - 1
        r, c = positions[last]
        if m[r][c] == "E":
            nbpaths += 1
            if mincost > cost:
                mincost = cost
            #print(f"{nbpaths:6} {mincost:7}", end="\r")
            #print(f"END {nbpaths:6} {mincost:7}")
            del positions[last]
            del directions[last]
            del turns[last]
            cost -= costs[last]
            del costs[last]
            backtrack = True
            continue
        dr, dc = directions[last]
        if not backtrack and cost < mincost:
            # Advance
            r2, c2 = r+dr, c+dc
            if m[r2][c2] in ".E" \
            and (r2,c2) not in positions \
            and len(positions) <= minlen[r2][c2] + 1000:
                minlen[r2][c2] = len(positions)
                positions.append((r2,c2))
                directions.append((dr,dc))
                turns.append(0)
                costs.append(1)
                cost += 1
                backtrack = False
                continue
        cplx = dr + dc*1j
        if turns[last] == 0:
            turns[last] = 1
            if True: #step % 2 == 0:
                turn = cplx * 1j
            else:
                turn = cplx * -1j
            costs[last] += 1000
            cost += 1000
        elif turns[last] == 1:
            turns[last] = 2
            turn = -cplx
        else:
            del positions[last]
            del directions[last]
            del turns[last]
            cost -= costs[last]
            del costs[last]
            backtrack = True
            continue
        # Turn
        tr, tc = int(turn.real), int(turn.imag)
        directions[last] = (tr,tc)
        backtrack = False
    return mincost

#mincost = dfs(m, Sr, Sc, 0, 1) # Going East
mincost = dfs(m) # Going East
print(mincost)
