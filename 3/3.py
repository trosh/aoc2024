#! /usr/bin/env python3

import sys
import re

s = sys.stdin.read()
tot = 0
do = True
for instr in re.findall(r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))', s):
    if instr == "do()":
        do = True
    elif instr == "don't()":
        do = False
    elif do:
        (a, b) = tuple(re.findall(r'\d+', instr))
        tot += int(a) * int(b)
print(tot)
