#! /usr/bin/env python3

import sys
import math
from collections import defaultdict

machines = []
machine = dict()
for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue
    left, right = line.split(": ")
    x, y = right.split(", ")
    if left.startswith("Button "):
        button = left.split()[1]
        x = int(x.split("+")[1])
        y = int(y.split("+")[1])
        machine[button] = (x,y)
    else:
        assert left == "Prize"
        x = int(x.split("=")[1])
        y = int(y.split("=")[1])
        machine[left] = (x, y)
        machines.append(machine)
        #print(machine)
        machine = dict()
print()

tot = 0
for machine in machines:
    #print(machine)
    ax, ay = machine["A"]
    bx, by = machine["B"]
    px, py = machine["Prize"]
    x, y = 0, 0
    ix = 0
    costmin = None
    cost1 = 0
    while x <= px and y <= py and ix < 100:
        xx, yy = x, y
        cost2 = cost1
        iy = 0
        while xx <= px and yy <= py and iy < 100:
            if xx == px and yy == py:
                #print(f"prize=({px},{py}) pos=({xx:04},{yy:04}) 3×{ix:02}+1×{iy:02}={cost2}")
                if costmin is None or cost2 < costmin:
                    costmin = cost2
            xx += bx
            yy += by
            cost2 += 1
            iy += 1
        x += ax
        y += ay
        cost1 += 3
        ix += 1
    if costmin is not None:
        tot += costmin
print(tot)
print()

tot = 0
for machine in machines:
    #print(machine)
    ax, ay = machine["A"]
    bx, by = machine["B"]
    px, py = machine["Prize"]
    px += 10000000000000
    py += 10000000000000
    #if 0 in [ax, ay, bx, by]:
    #    print("0, but don't give up")
    #if ay/ax > by/bx:
    #    # Exchange button vectors
    #    tx, ty = ax, ay
    #    ax, ay = bx, by
    #    bx, by = tx, ty
    #    print(f"exchange {ax},{ay} {bx},{by}")
    numer = px * ay - py * ax
    denom = bx * ay - by * ax
    #print(f"numer = {numer}")
    #print(f"denom = {denom}")
    if denom == 0:
        #print("denom == 0")
        continue
    if numer % denom != 0:
        #print(f"numer({numer}) % denom({denom}) != 0")
        continue
    nb = numer // denom
    if nb < 0:
        #print(f"nb({nb}) < 0")
        continue
    dx = px - nb * bx
    dy = py - nb * by
    if dx % ax != 0 or dy % ay != 0:
        #print(f"dx({dx}) % ax({ax}) or dy({dy}) % ay({ay})")
        continue
    na = dx // ax
    assert na == (dy // ay)
    #print(f"solution = {na}×a + {nb}×b")
    tot += na * 3 + nb * 1
print(tot)
