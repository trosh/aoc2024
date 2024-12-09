#! /usr/bin/env python3

import sys

def printfs(fs):
    for c in fs:
        print(c if c != -1 else ".", end="")
    print()

def defrag1(line):
    fs = []
    file_id = 0
    for i, n in enumerate(line):
        if i % 2 == 0:
            fs.extend([file_id] * n)
            file_id += 1
        else:
            fs.extend([-1] * n)
    #printfs(fs)
    i = len(fs) - 1
    j = 0
    while i >= j:
        if fs[i] == -1:
            del fs[i]
            i -= 1
        elif fs[j] != -1:
            j += 1
        else:
            fs[j] = fs[i]
            fs[i] = -1
            #del fs[i]
            i -= 1
            #printfs(fs)
        print(i, end="\r")
    return fs

def convert(fs):
    fs2 = []
    for i, l in fs:
        fs2.extend([i] * l)
    return fs2

def defrag2(line):
    fs = []
    file_id = 0
    for i, n in enumerate(line):
        if i % 2 == 0:
            fs.append((file_id, n))
            file_id += 1
        else:
            fs.append((-1, n))
    #printfs(convert(fs))
    i = len(fs) - 1
    while i > 0:
        i_id, i_len = fs[i]
        if i_id == -1:
            i -= 1
            continue
        for j in range(i):
            j_id, j_len = fs[j]
            if j_id != -1 or j_len < i_len:
                continue
            fs[j] = (i_id, i_len)
            fs[i] = (-1, i_len)
            if j_len > i_len:
                fs.insert(j+1, (-1, j_len-i_len))
                i += 1
            break
        i -= 1
        #printfs(convert(fs))
        print(i, end="\r")
    return convert(fs)

def checksum(fs):
    return sum(i*c if c != -1 else 0 for i,c in enumerate(fs))

line = [int(c) for c in sys.stdin.read().strip()]

fs1 = defrag1(line)
print("checksum1:", checksum(fs1))

fs2 = defrag2(line)
print("checksum2:", checksum(fs2))
