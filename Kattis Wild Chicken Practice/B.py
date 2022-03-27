from collections import Counter, defaultdict, deque
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


# ICPC Wild Chicken Practice B

n,m = input_int_gen()
edges = [set() for _ in range(n+1)]
in_edges = [set() for _ in range(n+1)]
for _ in range(m):
    u, v = input_int_gen()
    edges[u].add(v)
    in_edges[v].add(u)

roots = set()
for i in range(1, n+1):
    if not in_edges[i]:
        roots.add(i)
topo = []

while roots:
    xx = roots.pop()
    topo.append(xx)
    for neighbour in edges[xx]:
        in_edges[neighbour].remove(xx)
        if not in_edges[neighbour]:
            roots.add(neighbour)

topo.reverse()

longest = [0 for _ in range(n+1)]
second = [0 for _ in range(n+1)]
# print(topo)
for cur in topo:
    max1 = 0
    max2 = 0
    max1_set = set()
    for child in edges[cur]:
        c = longest[child] + 1
        d = max1
        if c < max2:
            continue
        if c == max1:
            max2 = max1
            max1_set.add(child)
        if c > max1:
            max2 = max1
            max1 = c
            max1_set = {child}
        else:
            max2 = c
    if len(max1_set) == 1:
        max2 = min(max2, max([second[mchild] for mchild in max1_set], default=-1)+1)
    longest[cur] = max1
    second[cur] = max2
print(longest,second)
a = max(longest)
max_set = set()
for cur in topo:
    if a == longest[cur]:
        max_set.add(cur)
max2 = a
if len(max_set) == 1:
    max2 = min(max2, max([second[mchild] for mchild in max_set], default=-1)+1)
print(max2)        

   