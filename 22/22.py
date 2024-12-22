#! /usr/bin/env python3

import sys

secrets = []
with open(sys.argv[1], "r") as f:
    for line in f:
        secrets.append(int(line.strip()))

for s in secrets:
    print(s)
print()

#prices = []
seqs = []
uniqchanges = set()
for i, s in enumerate(secrets):
    #prices.append([])
    seqs.append([])
    min4 = None
    min3 = None
    min2 = None
    min1 = None
    for x in range(2000):
        s ^= (s % 262144) << 6
        s ^= s >> 5
        s ^= (s % 8192) << 11
        secrets[i] = s
        price = s%10
        #prices[i].append(price)
        if min4 is not None:
            changes = (
                min3  - min4,
                min2  - min3,
                min1  - min2,
                price - min1,
            )
            seqs[i].append({"price" : price, "changes" : changes})
            uniqchanges.add(changes)
        min4 = min3
        min3 = min2
        min2 = min1
        min1 = price
for s in secrets:
    print(s)
print("sum", sum(secrets))
print("nb unique changes", len(uniqchanges))
most_bananas = 0
best_changes = None
for n, changes in enumerate(uniqchanges):
    print(changes, f"{100*n/len(uniqchanges):.2f}%")
    bananas = 0
    for seq in seqs:
        for pc in seq:
            if pc["changes"] == changes:
                bananas += pc["price"]
                break
    if most_bananas < bananas:
        most_bananas = bananas
        best_changes = changes
        print(most_bananas)

print(best_changes)
print(most_bananas)
