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

for bef in rules.keys():
    print(bef, "<", rules[bef])
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
    mid = len(update_sorted)//2
    val = update_sorted[mid]
    correct = True
    for (a, b) in zip(update, update_sorted):
        if a != b:
            correct = False
            break
    update_sorted = list(map(str, update_sorted))
    fmt =  ",".join(update_sorted[:mid])
    fmt += f",\033[31m{update_sorted[mid]}\033[37m,"
    fmt += ",".join(update_sorted[mid+1:])
    if correct:
        print(f"{fmt}")
        sum1 += val
    else:
        print(f"\033[7m{fmt}\033[m")
        sum2 += val

print(sum1)
print(sum2)
