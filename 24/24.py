#! /usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    links = dict()
    for line in f:
        line = line.strip()
        if line == "":
            break
        l, r = line.split(": ")
        links[l] = int(r)
    operations = list()
    for line in f:
        line = line.strip()
        operation, resline = line.split(" -> ")
        l, op, r = operation.split()
        operations.append((l, op, r, resline))

swaps = [
    ("z17", "cmv"),
    ("z30", "rdg"),
    ("btb", "mwp"),
    ("z23", "rmj"),
]
for x, y in swaps:
    for i, o in enumerate(operations):
        l, op, r, res = o
        if res == x:
            operations[i] = (l, op, r, "tmp")
            break
    for i, o in enumerate(operations):
        l, op, r, res = o
        if res == y:
            operations[i] = (l, op, r, x)
            break
    for i, o in enumerate(operations):
        l, op, r, res = o
        if res == "tmp":
            operations[i] = (l, op, r, y)
            break

alloperations = []
while True:
    remoperations = []
    for operation in operations:
        l, op, r, res = operation
        if l not in links or r not in links:
            remoperations.append(operation)
            continue
        lb = links[l]
        rb = links[r]
        if op == "XOR":
            resb = lb ^ rb
        elif op == "OR":
            resb = lb | rb
        else:
            assert op == "AND"
            resb = lb & rb
        links[res] = resb
        print(f"{l}({lb}) {op} {r}({rb}) -> {res}({resb})")
    alloperations += operations
    if remoperations == []:
        break
    operations = remoperations
operations = alloperations

Z = 0
for i, z in enumerate(sorted((l for l in links.keys() if l.startswith("z")))):
    print(z, links[z])
    if links[z] == 1:
        Z += 2 ** i
print(Z)

X = 0
Y = 0
for i in range(45):
    if links[f"x{i:02}"] == 1:
        X += 2 ** i
    if links[f"y{i:02}"] == 1:
        Y += 2 ** i
    p = 2 ** (i + 1)
    Zmod = Z % p
    print(i, X, Y, (X+Y)%p, Zmod)
    if Zmod != (X+Y)%p:
        break
print(X, Y, X+Y, Z)

print(",".join(sorted([s[0] for s in swaps] + [s[1] for s in swaps])))
