#! /usr/bin/env python3

import sys

m = []
def printm(m):
    for row in m:
        print("".join(row))
    print()

moves = []
R = 0
with open(sys.argv[1], "r") as f_in:
    for line in f_in:
        if line == "\n":
            break
        m.append([c for c in line.strip()])
        if "@" in line:
            (r,c) = (R, line.index("@"))
        R += 1
    C = len(m[0])
    printm(m)
    for line in f_in:
        moves.extend([d for d in line.strip()])

print(moves)

def copy(m):
    m2 = []
    for row in m:
        m2.append(row[:])
    return m2

m2 = copy(m)
printm(m2)

def trymove(m, r,c, d):
    print(f"trymove {r},{c} {d}")
    dr,dc = d
    r2,c2 = r+dr, c+dc
    x = m[r2][c2]
    if x == "#":
        return False
    if x == "." \
    or trymove(m, r2,c2, d):
        m[r2][c2] = m[r][c]
        m[r][c] = "."
        return True
    return False

for move in moves:
    print(move)
    if   move == "<": d = ( 0,-1)
    elif move == ">": d = ( 0, 1)
    elif move == "v": d = ( 1, 0)
    elif move == "^": d = (-1, 0)
    if trymove(m2, r,c, d):
        dr,dc = d
        r,c = r+dr, c+dc
    printm(m2)

tot = 0
for r, row in enumerate(m2):
    for c, x in enumerate(row):
        if x == "O":
            tot += 100*r + c
print(tot)

def copy(m):
    m2 = []
    global r, c
    for _r, row in enumerate(m):
        r2 = []
        for _c, x in enumerate(row):
            if x == ".":
                r2.append(".")
                r2.append(".")
            elif x == "#":
                r2.append("#")
                r2.append("#")
            elif x == "O":
                r2.append("[")
                r2.append("]")
            elif x == "@":
                r2.append("@")
                r2.append(".")
                r, c = _r, _c*2
        m2.append(r2)
    return m2

m2 = copy(m)
printm(m2)

def checkmove(m, r,c, d):
    print(f"checkmove {r},{c} {d}")
    dr,dc = d
    r2,c2 = r+dr, c+dc
    x = m[r2][c2]
    if x == "#":
        return False
    elif x == ".":
        return True
    elif x == "[":
        if dc == 0:
            if not checkmove(m, r2,c2,   d): return False
            if not checkmove(m, r2,c2+1, d): return False
        else:
            assert dc == 1
            if not checkmove(m, r2,c2+1, d): return False
    else:
        assert x == "]"
        if dc == 0:
            if not checkmove(m, r2,c2,   d): return False
            if not checkmove(m, r2,c2-1, d): return False
        else:
            assert dc == -1
            if not checkmove(m, r2,c2-1, d): return False
    return True

def domove(m, r,c, d):
    print(f"domove {r},{c}, {d}")
    dr,dc = d
    r2,c2 = r+dr, c+dc
    x = m[r2][c2]
    assert x != "#"
    if x == ".":
        m[r2][c2] = m[r][c]
        m[r][c] = "."
    elif x == "[":
        if dc == 0:
            domove(m, r2,c2,   d)
            domove(m, r2,c2+1, d)
            m[r2][c2  ] = m[r][c]
            m[r2][c2+1] = "."
            m[r ][c   ] = "."
        else:
            assert dc == 1
            domove(m, r2,c2+1, d)
            m[r2][c2+1] = m[r2][c2]
            m[r2][c2] = m[r][c]
            m[r][c] = "."
    else:
        assert x == "]"
        if dc == 0:
            domove(m, r2,c2,   d)
            domove(m, r2,c2-1, d)
            m[r2][c2  ] = m[r][c]
            m[r2][c2-1] = "."
            m[r ][c   ] = "."
        else:
            assert dc == -1
            domove(m, r2,c2-1, d)
            m[r2][c2-1] = m[r2][c2]
            m[r2][c2] = m[r][c]
            m[r][c] = "."

for move in moves:
    print(move)
    if   move == "<": d = ( 0,-1)
    elif move == ">": d = ( 0, 1)
    elif move == "v": d = ( 1, 0)
    elif move == "^": d = (-1, 0)
    if checkmove(m2, r,c, d):
        domove(m2, r,c, d)
        dr,dc = d
        r,c = r+dr, c+dc
    printm(m2)

tot = 0
for r, row in enumerate(m2):
    for c, x in enumerate(row):
        if x == "[":
            tot += 100*r + c
print(tot)
