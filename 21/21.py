#! /usr/bin/env python3

import sys
import math
from collections import defaultdict

def debug_signal_handler(signal, frame):
    import pdb
    pdb.set_trace()
import signal
signal.signal(signal.SIGINT, debug_signal_handler)

numpad = {
	"A" : (3, 2),
	"0" : (3, 1),
	"1" : (2, 0),
	"2" : (2, 1),
	"3" : (2, 2),
	"4" : (1, 0),
	"5" : (1, 1),
	"6" : (1, 2),
	"7" : (0, 0),
	"8" : (0, 1),
	"9" : (0, 2),
}

dirpad = {
	">" : (1, 2),
	"<" : (1, 0),
	"v" : (1, 1),
	"^" : (0, 1),
	"A" : (0, 2),
}

padpad = {
    "AA" : "A",
    "A^" : "<A",
    "A>" : "vA",
    "Av" : "<vA",
    "A<" : "v<<A",
    "^A" : ">A",
    "^^" : "A",
    "^>" : "v>A",
    "^v" : "vA",
    "^<" : "v<A",
    ">A" : "^A",
    ">^" : "<^A",
    ">>" : "A",
    ">v" : "<A",
    "><" : "<<A",
    "vA" : "^>A",
    "v^" : "^A",
    "v>" : ">A",
    "vv" : "A",
    "v<" : "<A",
    "<A" : ">>^A",
    "<^" : ">^A",
    "<>" : ">>A",
    "<v" : ">A",
    "<<" : "A",
}

dirkey = {
	(0, 1) : ">",
	(0,-1) : "<",
	(1, 0) : "v",
	(-1,0) : "^",
}

codes = []
with open(sys.argv[1], "r") as f:
	for line in f:
		codes.append(line.strip())

def check(r, c, seq):
    for dr,dc in seq:
        r,c = r+dr, c+dc
        if (r,c) == (3,0):
            return False
    return True

memo = defaultdict(dict)

def robot(n, seq):
    curkey = "A"
    r, c = dirpad[curkey]
    len2 = 0
    subseqs = ""
    for key in seq:
        r2, c2 = dirpad[key]
        move = curkey + key
        subseq = padpad[move]
        subseqs += subseq
        if subseq in memo and n in memo[move]:
            sublen = memo[move][n]
        else:
            if n == 0:
                sublen = len(subseq)
            else:
                sublen = robot(n - 1, subseq)
            memo[move][n] = sublen
        len2 += sublen
        curkey = key
        r, c = r2, c2
    return len2

total = 0
for code in codes:
    print(code)
    r, c = numpad["A"]
    seq1 = ""
    for num in code:
        r_, c_ = numpad[num]
        dr, dc = r_-r, c_-c
        sr = 1 if dr >= 0 else -1
        sc = 1 if dc >= 0 else -1
        hori = [(0, sc)] * abs(dc) + [(sr, 0)] * abs(dr)
        vert = [(sr, 0)] * abs(dr) + [(0, sc)] * abs(dc)
        needcheck = (dr != 0 and dc != 0)
        if needcheck:
            if not check(r, c, hori):
                print("must vert")
                dirs = vert
            elif not check(r, c, vert):
                print("must hori")
                dirs = hori
            elif c_ < c:
                print("go left, hori")
                dirs = hori
            else:
                print("default vert")
                dirs = vert
        else:
            print("no choice")
            dirs = hori
        subseq = "".join((dirkey[d] for d in dirs)) + "A"
        print(num, subseq)
        seq1 += subseq
        r, c = r_, c_
    print(seq1)
    minlen = robot(24, seq1)
    print(code)
    print( int(code[:-1]) , minlen )
    cplx = int(code[:-1]) * minlen
    print(cplx)
    total += cplx

print("total", total)
