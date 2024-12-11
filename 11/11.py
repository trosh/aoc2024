#! /usr/bin/env python3

import sys

stones = [int(n) for n in sys.stdin.read().strip().split()]

print(stones)
for blink in range(75):
    i = len(stones)-1
    while i >= 0:
        stone = stones[i]
        if stone == 0:
            stones[i] = 1
        else:
            pow10 = 10
            ndigits = 1
            while pow10 < stone:
                pow10 *= 10
                ndigits += 1
            #print(stone, ndigits)
            if ndigits % 2 == 0:
                pow10 = 10 ** (ndigits//2)
                stones[i] %= pow10
                stones.append(stone//pow10)
                #stones.insert(i, stone//pow10)
            else:
                stones[i] *= 2024
        i -= 1
    print(blink, len(stones), end="\r")
print(len(stones))
