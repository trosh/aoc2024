#! /usr/bin/env python3

import sys
from collections import defaultdict
from random import choice

id2name = dict()
name2id = dict()
nbid = 0
neighbours = defaultdict(set)
edges = list()
with open(sys.argv[1], "r") as f:
    for line in f:
        l, r = line.strip().split("-")
        if l not in name2id:
            lid = nbid
            name2id[l] = lid
            id2name[lid] = l
            nbid += 1
        else:
            lid = name2id[l]
        if r not in name2id:
            rid = nbid
            name2id[r] = rid
            id2name[rid] = r
            nbid += 1
        else:
            rid = name2id[r]
        neighbours[lid].add(rid)
        neighbours[rid].add(lid)
        if rid < lid:
            lid, rid = rid, lid
        edges.append((lid,rid))

# spanning tree with BFS
span = list()
seen = set()
root = edges[0][0]
todo = [root]
while todo != []:
    cur = todo
    todo = []
    for node in cur:
        for node2 in neighbours[node]:
            if node2 in seen:
                continue
            seen.add(node2)
            todo.append(node2)
            l, r = node, node2
            if r < l:
                l, r = r, l
            span.append((l,r))
# 3-cycles with 't.'
cycles = set()
for edge in edges:
    l, r = edge
    if edge in span:
        continue
    for oe1 in neighbours[l]:
        for oe2 in neighbours[r]:
            if oe1 != oe2:
                continue
            if  id2name[l  ][0] != "t" \
            and id2name[r  ][0] != "t" \
            and id2name[oe1][0] != "t":
                continue
            cycle = tuple(sorted((l, r, oe1)))
            if cycle in cycles:
                continue
            cycles.add(cycle)
            print(",".join(map(lambda i: id2name[i], cycle)))
print(len(cycles))

def names(group):
    if group == []:
        return ""
    return ",".join(sorted(map(lambda i: id2name[i], group)))

maxcliques = []
def BronKerbosch2(R, P, X):
    if len(P) == 0 and len(X) == 0:
        maxcliques.append(R)
        print(names(R))
        return
    u = choice(list(P | X))
    for v in P - neighbours[u]:
        BronKerbosch2(
            R | {v},
            P & neighbours[v],
            X & neighbours[v])
        P.remove(v)
        X.add(v)

def BronKerbosch3(neighbours):
    P = set(neighbours.keys())
    R = set()
    X = set()
    for v in sorted(P, key=lambda n: len(neighbours[n])):
        BronKerbosch2(
            R | {v},
            P & neighbours[v],
            X & neighbours[v])
        P.remove(v)
        X.add(v)

BronKerbosch3(neighbours)
for clique in sorted(maxcliques, key=len):
    print(names(clique))

#def searchLAN(neighbours, group):
#    new = neighbours[group[0]] - set(group)
#    print("new", names(new))
#    for i in range(1, len(group)):
#        node = group[i]
#        new &= neighbours[node]
#        print("intersection update", names(neighbours[node]), names(new))
#    if len(new) > 0:
#        newgroup = tuple(sorted(list(group) + list(new)))
#        print(names(group))
#        print("\t", names(newgroup))
#        return newgroup
#    return None
#
#def are_separate(ga, gb):
#    for x in ga:
#        if x in gb:
#            return False
#    return True
#
#def are_bipartite(ga, gb):
#    for x in ga:
#        for y in gb:
#            if y not in neighbours[x]:
#                return False
#    return True
#
#groups = [(x,) for x in neighbours.keys()]
#newgroups = edges[:]
#maxlen = 2
#while True:
#    nextgroups = []
#    niter = len(groups) * len(newgroups)
#    curiter = 0
#    for ga in newgroups:
#        for gb in groups:
#            if curiter % 50000 == 0 and nextgroups != []:
#                print(f"\033[K{100*curiter/niter:.2f}% {names(nextgroups[-1])}", end="\r")
#            curiter += 1
#            if not are_separate (ga, gb) \
#            or not are_bipartite(ga, gb):
#                continue
#            newgroup = tuple(sorted(list(ga) + list(gb)))
#            if newgroup in groups:
#                continue
#            if maxlen < len(newgroup):
#                maxlen = len(newgroup)
#                print("\033[K", maxlen, names(newgroup))
#            nextgroups.append(newgroup)
#    groups.extend(newgroups)
#    groups.sort(reverse=True)
#    newgroups = sorted(nextgroups, reverse=True)

#while todo != []:
#    cur = todo
#    todo = []
#    for i, group in enumerate(cur):
#        print(f"{100*i/len(cur):.2f}% {names(group)} {len(longests)}")
#        group2 = searchLAN(neighbours, group)
#        if group2 is None or group2 in groups:
#            continue
#        todo.append(group2)
#        if longests == [] or len(longests[0]) < len(group2):
#            longests = [group2]
#        elif len(longests[0]) == len(group2):
#            longests.append(group2)
#        for longest in longests:
#            print("longest:", names(longest))
#    groups.extend(todo)
#for longest in longests:
#    print("longest:", names(longest))
