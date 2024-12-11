#! /usr/bin/env python3

import sys
from collections import defaultdict

stones = [int(n) for n in sys.stdin.read().strip().split()]

S = defaultdict(int)
for stone in stones:
    S[stone] += 1
print(S)

print(stones)
for blink in range(1, 76):
    S2 = defaultdict(int)
    for stone in S:
        count = S[stone]
        if stone == 0:
            S2[1] += count
        else:
            pow10 = 10
            ndigits = 1
            while pow10 <= stone:
                pow10 *= 10
                ndigits += 1
            if ndigits % 2 == 0:
                pow10 = 10 ** (ndigits//2)
                S2[stone  % pow10] += count
                S2[stone // pow10] += count
            else:
                S2[stone * 2024] += count
    S = S2
    tot = 0
    for stone in S:
        tot += S[stone]
    print(blink, tot)
print()
