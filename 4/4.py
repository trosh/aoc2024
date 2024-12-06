#! /usr/bin/env python3

import sys
import re

a=[]
for l in sys.stdin:
    a.append(l.strip())
print(a)
R=len(a)
C=len(a[0])

l=0
def xmas(s):
    print(s)
    return len(re.findall("XMAS", s))+len(re.findall("XMAS", s[::-1]))

for r in range(R):
    cc=0
    rr=r
    s=""
    while rr>=0 and rr<R and cc>=0 and cc<C:
        s+=a[rr][cc]
        cc+=1
    l+=xmas(s)
    cc=0
    rr=r
    s=""
    while rr>=0 and rr<R and cc>=0 and cc<C:
        s+=a[rr][cc]
        cc+=1
        rr+=1
    l+=xmas(s)
    cc=0
    rr=r
    s=""
    while rr>=0 and rr<R and cc>=0 and cc<C:
        s+=a[rr][cc]
        cc+=1
        rr-=1
    l+=xmas(s)

for c in range(1,C):
    cc=c
    rr=0
    s=""
    while rr>=0 and rr<R and cc>=0 and cc<C:
        s+=a[rr][cc]
        rr+=1
    l+=xmas(s)
    cc=c
    rr=0
    s=""
    while rr>=0 and rr<R and cc>=0 and cc<C:
        s+=a[rr][cc]
        cc+=1
        rr+=1
    l+=xmas(s)
    cc=c
    rr=R-1
    s=""
    while rr>=0 and rr<R and cc>=0 and cc<C:
        s+=a[rr][cc]
        cc+=1
        rr-=1
    l+=xmas(s)

print(l)
