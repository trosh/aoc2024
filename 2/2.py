#! /usr/bin/env python3

import sys

def comp(a, b, inc):
    diff = b - a
    if inc:
        if diff not in [ 1,  2,  3]:
            return False
    else:
        if diff not in [-1, -2, -3]:
            return False
    return True

def check(report):
    inc = True if report[1] > report[0] else False
    for i in range(len(report) - 1):
        if not comp(report[i], report[i+1], inc):
            return False
    return True

nb_safe = 0
nb_safe_dampened = 0
for line in sys.stdin:
    report = list(map(int, line.strip().split()))
    if check(report):
        nb_safe += 1
    else:
        for i in range(len(report)):
            dampened_report = report[:i] + report[i+1:]
            if check(dampened_report):
                nb_safe_dampened += 1
                break

print(nb_safe)
print(nb_safe + nb_safe_dampened)
