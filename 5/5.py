#! /usr/bin/env python3

import sys
from collections import defaultdict
from functools import cmp_to_key

rules = defaultdict(list)
updates = []

readrules = False
for line in sys.stdin:
    line.strip()
    if line == "\n":
        readrules = True
        continue
    if not readrules:
        (bef, aft) = map(int, line.split("|"))
        rules[bef].append(aft)
    else:
        updates.append(list(map(int, line.split(","))))

print(rules)
for update in updates:
    print(update)
print()

def cmp(x, y):
    if y in rules[x]:
        return -1
    if x in rules[y]:
        return 1
    return 0

sum1 = 0
sum2 = 0

for update in updates:
    update_sorted = sorted(update, key=cmp_to_key(cmp))
    mid = update_sorted[len(update_sorted)//2]
    correct = True
    for (a, b) in zip(update, update_sorted):
        if a != b:
            correct = False
            break
    if correct:
        sum1 += mid
    else:
        sum2 += mid

print(sum1)
print(sum2)
