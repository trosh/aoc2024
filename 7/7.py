#! /usr/bin/env python3

import sys
import itertools

eqs = list()

for line in sys.stdin:
	(res, ops) = line.strip().split(": ")
	eqs.append((int(res), list(map(int, ops.split()))))
#print(eqs)
def f(operators):
    sumok = 0
    for n, (res, operands) in enumerate(eqs):
        print(f"{n*100//len(eqs)}%   ",end="\r")
        nb_operators = len(operands) - 1
        #print(res, end=": ")
        done=False
        for seq in itertools.product(operators, repeat=nb_operators):
            #print(res, end=": ")
            tstres = operands[0]
            #print(operands[0], end=" ")
            i = 0
            for operator in seq:
                if operator == "*":
                    #print(f"\033[41m{operator}\033[m", end=" ")
                    tstres *= operands[i+1]
                elif operator == "+":
                    #print(f"\033[42m{operator}\033[m", end=" ")
                    tstres += operands[i+1]
                elif operator == "|":
                    #print(f"\033[43m{operator}\033[m", end=" ")
                    tstres = int(str(tstres)+str(operands[i+1]))
                #print(operands[i+1], end=" ")
                i += 1
                if tstres > res:
                    break
            if tstres == res:
                if not done:
                    sumok += res
                    done=True
                #print("\033[7mok\033[m")
            #else:
                #print(tstres)
        #print()
    print(sumok)

f("+*")
f("+*|")
