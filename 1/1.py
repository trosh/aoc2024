#! /usr/bin/env python3

L = []
R = []
with open("input.txt", "r") as f:
    for line in f:
        (l, r) = map(int, line.strip().split())
        L.append(l)
        R.append(r)

L.sort()
R.sort()

total_dist = 0
for l, r in zip(L, R):
    dist = abs(l-r)
    print(l, r, abs(l-r))
    total_dist += dist
print(total_dist)

total_similarity = 0
for l in L:
    c = 0
    for r in R:
        if r == l:
            c += 1
    similarity = l * c
    total_similarity += similarity

print(total_similarity)
