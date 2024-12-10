#! /usr/bin/env python3

import sys

m = []
for line in sys.stdin:
    m.append([int(n) for n in line.strip()])

def printm(m):
    for line in m:
        print("".join((str(n) if n is not None else "." for n in line)))
    print()

printm(m)

def dup(m):
    m2 = []
    for line in m:
        m2.append(line[:])
    return m2

R = len(m)
C = len(m[0])

def inside(r, c):
    if 0<=r<R and 0<=c<C:
        return True
    return False

def search(m, seen, r, c, h):
    if seen[r][c] is not None \
    or m[r][c] != h + 1:
        return h
    seen[r][c] = m[r][c]
    max_h = m[r][c]
    if max_h == 9:
        return max_h
    for r2, c2 in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
        if inside(r2, c2):
            nh = search(m, seen, r2, c2, m[r][c])
            if nh > max_h:
                max_h = nh
    return max_h

tot = 0
for r in range(R):
    for c in range(C):
        if m[r][c] != 0:
            continue
        #m2 = dup(m)
        seen = [[None]*C for r in range(R)]
        max_h = search(m, seen, r, c, -1)
        printm(seen)
        if max_h < 9:
            continue
        subtot = 0
        for r2 in range(R):
            for c2 in range(C):
                if seen[r2][c2] and m[r2][c2] == 9:
                    subtot += 1
        print(subtot)
        tot += subtot
print(tot)

def search2(m, r, c, h):
    #if seen[r][c] is not None or \
    if m[r][c] != h + 1:
        return 0
    #seen[r][c] = m[r][c]
    if m[r][c] == 9:
        return 1
    npaths = 0
    for r2, c2 in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
        if inside(r2, c2):
            nh = search2(m, r2, c2, m[r][c])
            npaths += nh
    return npaths

tot = 0
for r in range(R):
    for c in range(C):
        if m[r][c] != 0:
            continue
        #m2 = dup(m)
        npaths = search2(m, r, c, -1)
        if npaths == 0:
            continue
        tot += npaths
print(tot)

