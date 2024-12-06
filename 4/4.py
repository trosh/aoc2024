#! /usr/bin/env python3

import sys
import re

a = []
for l in sys.stdin:
    a.append(l.strip())
print("\n".join(a))
R = len(a)
C = len(a[0])

def inside(r, c):
    if r < 0 or r >= R \
    or c < 0 or c >= C:
        return False
    return True

b = list((list((" " for bb in aa)) for aa in a))
for bb in b:
    print("".join(bb))

x = 0
def check(it):
    l = 0
    global x
    x += 1
    for posl in it():
        s = "".join((a[r][c] for (r, c) in posl))
        #print(s)
        for m in re.finditer("XMAS", s):
            l += 1
            #print(m)
            for (r, c) in posl[m.start():m.start()+4]:
                b[r][c] = f"\033[3{x}m{a[r][c]}\033[m"
        for m in re.finditer("XMAS", s[::-1]):
            l += 1
            #print(m)
            for (r, c) in posl[-m.start()-1:-m.start()-5:-1]:
                b[r][c] = f"\033[1;3{x}m{a[r][c]}\033[m"
    return l

def iter_rows():
    for r in range(R):
        posl = []
        c = 0
        while inside(r, c):
            posl.append((r, c))
            c += 1
        yield posl

def iter_cols():
    for c in range(C):
        posl = []
        r = 0
        while inside(r, c):
            posl.append((r, c))
            r += 1
        yield posl

def iter_diagnwse():
    for r in range(R):
        posl = []
        c = 0
        while inside(r, c):
            posl.append((r, c))
            c += 1
            r += 1
        yield posl
    for c in range(1, C):
        posl = []
        r = 0
        while inside(r, c):
            posl.append((r, c))
            r += 1
            c += 1
        yield posl

def iter_diagswne():
    for r in range(R):
        posl = []
        c = 0
        while inside(r, c):
            posl.append((r, c))
            c += 1
            r -= 1
        yield posl
    for c in range(1, C):
        posl = []
        r = R - 1
        while inside(r, c):
            posl.append((r, c))
            r -= 1
            c += 1
        yield posl

check(iter_rows)
for bb in b:
    print("".join(bb))
b = list((list((" " for bb in aa)) for aa in a))
check(iter_cols)
for bb in b:
    print("".join(bb))
b = list((list((" " for bb in aa)) for aa in a))
check(iter_diagnwse)
for bb in b:
    print("".join(bb))
b = list((list((" " for bb in aa)) for aa in a))
check(iter_diagswne)
for bb in b:
    print("".join(bb))
x = 0
b = list((list((" " for bb in aa)) for aa in a))

l = 0
for it in [
        iter_rows, iter_cols,
        iter_diagnwse, iter_diagswne,
        ]:
    l += check(it)

for (aa, bb) in zip(a, b):
    #print(aa)
    print("".join(bb))
print("num matches XMAS:", l)

b = list((list((" " for bb in aa)) for aa in a))
l = 0
for r in range(R-2):
    for c in range(C-2):
        d1 = a[r  ][c] + a[r+1][c+1] + a[r+2][c+2]
        d2 = a[r+2][c] + a[r+1][c+1] + a[r  ][c+2]
        if  (d1 == "MAS" or d1 == "SAM") \
        and (d2 == "MAS" or d2 == "SAM"):
            l += 1
            b[r  ][c  ] = a[r  ][c  ]
            b[r+1][c+1] = a[r+1][c+1]
            b[r+2][c+2] = a[r+2][c+2]
            b[r+2][c  ] = a[r+2][c  ]
            b[r  ][c+2] = a[r  ][c+2]
for bb in b:
    print("".join(bb))
print("num matches X-MAS:", l)
