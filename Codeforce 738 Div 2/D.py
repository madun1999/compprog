import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_list():
    # list of integers
    return list(map(int,input().split()))
def input_string():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())

#### disjoint sets #### https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d
def find(data, i):
    if data[i] != -1:
        data[i] = find(data, data[i])
        return data[i]
    return i
def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj
def connected(data, i, j):
    return find(data, i) == find(data, j)

#### disjoint sets with lookup #### https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d
def group_find(data, lookup, i):
    if data[i] != -1:
        data[i] = find(data, data[i])
        return data[i]
    if i not in lookup or not lookup[i]:
        lookup[i] = {i}
    return i
def group_union(data, lookup, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj
        lookup[pj] = group_lookup(data, lookup, pi) | group_lookup(data, lookup, pj)
        del lookup[pi]
def group_connected(data, lookup, i, j):
    return find(data, i) == find(data, j)
def group_lookup(data, lookup, i):
    # assume i is a parent
    assert data[i] == -1
    if i not in lookup or not lookup[i]:
        lookup[i] = {i}
    return lookup[i]

# Codeforce 738 Div 2 D
from collections import defaultdict
n, m1, m2 = input_int_gen()
if m1 == n - 1 or m2 == n - 1:
    print(0)
    exit()

to_add = min(n-1-m1, n-1-m2)
print(to_add)
if n == 2:
    print(1,2)
    exit()

dsA = defaultdict(lambda:-1)
lookupA = defaultdict(set) # lookup
dsB = defaultdict(lambda:-1)
lookupB = defaultdict(set) # lookup

gdata = defaultdict(lambda:-1) # data
glookup = defaultdict(set) # lookup


for _ in range(m1):
    a,b = input_int_gen()
    group_union(dsA, lookupA, a, b)


for _ in range(m2):
    a,b = input_int_gen()
    group_union(dsB, lookupB, a, b)
    if connected(dsA, a, b):
        group_union(gdata, glookup, a, b)

while to_add > 0:
    pa = next(x for x,y in lookupA.items() if len(y) >= 2, default=None)
    if pa is None:
        


