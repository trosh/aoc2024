#! /usr/bin/env python3

import sys

towels = dict()

def getpfx(p, s):
    for c in s:
        if c not in p:
            return None
        p = p[c]
    return p

def addpfx(p, s):
    for c in s:
        if c not in p:
            p[c] = dict()
        p = p[c]
    return p

with open(sys.argv[1], "r") as f:
    for word in f.readline().strip().split(", "):
        t = addpfx(towels, word)
        t["."] = True # terminator
    f.readline() # empty
    designs = []
    for line in f:
        line = line.strip()
        designs.append(line)

def print_towels(t, indent):
    for c in t:
        print(f"{indent}{c}")
        if c != ".":
            print_towels(t[c], indent+" ")
print_towels(towels, "")

def dfs(design):
    t = towels
    for i, c in enumerate(design):
        if c not in t:
            break
        if "." in t[c]:
            if dfs(design[i+1:]):
                return True
        t = t[c]
    else:
        return True
    return False

cando = 0
for design in designs:
    print(design)
    if dfs(design):
        cando += 1
print(cando)

pfxcando = dict()

def dfs2(start, design):
    print(start, design, end="\r")
    p = getpfx(pfxcando, design)
    if p is not None:
        if "." in p:
            return p["."]
    t = towels
    cando = 0
    newstart = start
    for i, c in enumerate(design):
        newstart += c
        if c not in t:
            break
        if "." in t[c]:
            if i == len(design) - 1:
                cando += 1
            else:
                rest = design[i+1:]
                p = getpfx(pfxcando, rest)
                if p is not None and "." in p:
                    subcando = p["."]
                else:
                    subcando = dfs2(newstart, rest)
                    addpfx(pfxcando, rest)["."] = subcando
                cando += subcando
        t = t[c]
    else:
        print(start, design, cando)
        p = addpfx(pfxcando, design)
        p["."] = cando
        return cando
    return cando

cando = 0
for design in designs:
    print(design)
    subcando = dfs2("", design)
    print()
    print(subcando)
    cando += subcando
print(cando)

