#! /usr/bin/env python3

import sys

m = []
for n, line in enumerate(sys.stdin):
    l = line.strip()
    m.append([c for c in l])
    if "^" in l:
        r1 = n
        c1 = l.index("^")
for line in m:
    print("".join(line))
print(r1, c1)

def copy(m1):
    m2 = []
    for line in m1:
        m2.append(line[:])
    return m2

R = len(m)
C = len(m[0])
def inside(rc):
    (r, c) = rc
    if r < 0 or r >= R \
    or c < 0 or c >= C:
        return False
    return True

def traverse(m, r, c):
    prev = []
    d = m[r][c]
    assert(d in "<>v^")
    while True:
        m[r][c] = "X"
        if d == "^":
            rc = (r-1, c)
        elif d == ">":
            rc = (r, c+1)
        elif d == "v":
            rc = (r+1, c)
        else: # <
            rc = (r, c-1)
        if not inside(rc):
            return False
        if m[rc[0]][rc[1]] in "#O":
            if (rc[0],rc[1],d) in prev:
                return True
            prev.append((rc[0],rc[1],d))
            if d == "^":
                d = ">"
            elif d == ">":
                d = "v"
            elif d == "v":
                d = "<"
            else: # <
                d = "^"
        else:
            (r, c) = rc

m2 = copy(m)
traverse(m2, r1, c1)
for line in m2:
    print("".join(line))
n = sum(sum(char == "X" for char in row) for row in m2)
print(f"Number of distinct positions: {n}")

n = 0
for r in range(R):
    for c in range(C):
        if m2[r][c] != "X" or m[r][c] == "^":
            continue
        m3 = copy(m)
        m3[r][c] = "O"
        if traverse(m3, r1, c1):
            n += 1
            for line in m3:
                print("".join(line))
            print()
print(f"Number of loop obstructions: {n}")
