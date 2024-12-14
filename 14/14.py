#! /usr/bin/env python3

import sys
from collections import defaultdict
from time import sleep

X = None
Y = None
niter = 100
cnt_tl = 0
cnt_tr = 0
cnt_bl = 0
cnt_br = 0
g = defaultdict(list)
for line in sys.stdin:
    p, v = line.strip().split()
    px, py = map(int, p.split("=")[1].split(","))
    vx, vy = map(int, v.split("=")[1].split(","))
    g[(px,py)].append((vx,vy))
    if X is None:
        if px == 0:
            X = 11
            Y = 7
        else:
            X = 101
            Y = 103
    print(px, py, vx, vy)
    px100 = (px + 100 * vx) % X
    py100 = (py + 100 * vy) % Y
    print(px100, py100)
    top, bottom = False, False
    if py100 < Y // 2:
        top = True
    elif py100 > Y // 2:
        bottom = True
    if px100 < X // 2:
        if top:
            print("top left")
            cnt_tl += 1
        elif bottom:
            print("bottom left")
            cnt_bl += 1
    elif px100 > X // 2:
        print(top, bottom)
        if top:
            print("top right")
            cnt_tr += 1
        elif bottom:
            print("bottom right")
            cnt_br += 1
    print()
print(cnt_tl * cnt_tr * cnt_bl * cnt_br)

niter = 0
while True:
    nbleft = 0
    for x in range(3):
        for y in range(Y):
            if (x,y) in g:
                nbleft += 1
    if nbleft < 10:
        for y in range(Y):
            for x in range(X):
                if (x,y) not in g:
                    print(".", end="")
                else:
                    print(len(g[(x,y)]), end="")
            print()
        print(niter)
        sleep(0.15)
    g2 = defaultdict(list)
    for px,py in g:
        for (vx,vy) in g[(px,py)]:
            g2[((px+vx)%X,(py+vy)%Y)].append((vx,vy))
    g = g2
    niter += 1
