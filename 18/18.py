#! /usr/bin/env python3

Ex = []
with open("ex", "r") as f:
    for line in f:
        Ex.append(tuple(map(int, line.strip().split(","))))
In = []
with open("in", "r") as f:
    for line in f:
        In.append(tuple(map(int, line.strip().split(","))))

def part1(blocks, side, nfall):
    m = [["."] * side for _ in range(side)]
    for block in blocks[:nfall]:
        c,r = block
        m[r][c] = "#"
    def inside(r, c):
        return 0<=r<side and 0<=c<side
    # BFS
    niter = 0
    todo = [(0,0)]
    m[0][0] = "O"
    while todo != []:
        #for line in m:
        #    print("".join(line))
        #print()
        #print(todo)
        cur = todo
        todo = []
        for r, c in cur:
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                r2, c2 = r+dr, c+dc
                if not inside(r2, c2):
                    continue
                if (r2, c2) == (side-1, side-1):
                    return niter + 1
                if m[r2][c2] != ".":
                    continue
                todo.append((r2,c2))
                m[r2][c2] = "O"
        niter += 1
    return -1

print(part1(Ex,  7,   12))
print(part1(In, 71, 1024))

for i, block in enumerate(Ex):
    if part1(Ex, 7, i+1) == -1:
        print(block)
        break

for i, block in enumerate(In):
    print(block)
    if part1(In, 71, i+1) == -1:
        print(block)
        break
