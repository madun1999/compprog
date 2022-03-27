from collections import defaultdict, Counter
import heapq
from itertools import combinations
from bisect import bisect_left, bisect_right

################### Read template ################
import sys
input = sys.stdin.readline
def inp(): 
    # one integer
    return int(input())

def input_list_int():
    # list of integers
    return list(map(int,input().split()))

def input_list_char():
    # list of characters
    s = input()
    return s[:-1]

def input_string():
    # list of characters
    s = input()
    # return list(s[:len(s) - 1])
    return s[:-1]

def input_list_string():
    # list of characters
    s = input()
    return list(s[:-1])
    
def input_int_gen():
    # integer generator 
    return map(int,input().split())
    
def input_float_gen():
    # float generator 
    return map(float,input().split())


############# Graphs ##################
# read graph template
# read graph without weight
n, m = input_int_gen()
edges = [set() for _ in range(n+1)] 
for _ in range(m):
    u, v = input_int_gen()
    edges[u].add(v)
    edges[v].add(u) # for undirected

# read directed graph without weight with in-degree
n, m = input_int_gen()
edges = [set() for _ in range(n+1)] 
inedges = [set() for _ in range(n+1)] 
for _ in range(m):
    u, v = input_int_gen()
    edges[u].add(v)
    inedges[v].add(u)

# read graph with weight
from collections import defaultdict
n, m = input_int_gen()
edges = [defaultdict(int) for _ in range(n+1)] # if edges have weights
for _ in range(m):
    u, v, w = input_int_gen()
    edges[u][v] = w
    edges[v][u] = w # for undirected


# dijkstra
from heapq import heappush, heappop
def dijkstra(edges, source, n): # edges must be weighted
    h = [(0,source)] # heap
    ds = [float("inf") for _ in range(n+1)] # calculated distances
    ds[source] = 0 #
    while h:
        vdis, v = heappop(h) 
        if vdis > ds[v]:
            continue
        for u, uvdis in edges[v].items():
            if uvdis >= 0 and ds[v] + uvdis < ds[u]: # update distance if shorter found
                ds[u] = ds[v] + uvdis
                heappush(h, (ds[u], u))
    return ds # distance from source to all points, infinity for other indices, especially index 0 

# topological sort (needs inedges)
def toposort(edges, inedges, n): 
    # returns topologically sorted vertices, must be directed graph, 
    # returns None if the graph contains a cycle
    ss = []
    ret = []
    indeg = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        indeg[i] = len(inedges[i])
        if indeg[i] == 0:
            ss.append(i)
    while ss:
        u = ss.pop()
        ret.append(u)
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                ss.append(v)
    return None if len(ret) != n else ret

# tree bfs template, gives parents, children
stk = [(1, False, -1)]
counts = [0 for _ in range(n+1)] 
parents = [0 for _ in range(n+1)]
children = [set() for _ in range(n+1)]
while stk:
    node, visited, par = stk.pop()
    # print(node, visited, par)
    if visited:
        children[node] = set(t for t in edges[node] if t != par)
        counts[node] = 1 + sum(counts[t] for t in children[node])
        parents[node] = par
    else:
        stk.append((node, True, par))
        for x in edges[node]:
            if x != par:
                stk.append((x, False, node))


################ disjoint sets ##################
# union find, union by size
# ufd = union_find_data
# initialize data, index 0~n inclusive
def make_ufd(n):
    return ([x for x in range(n+1)], [1 for _ in range(n+1)])

def find(ufd, i):
    data, _ = ufd
    root = i
    while data[root] != root:
        root = data[root]
    while data[i] != root:
        p = data[i]
        data[i] = root
        i = p
    return root

def union(ufd, i, j):
    data, size = ufd
    pi, pj = find(ufd, i), find(ufd, j)
    if pi == pj:
        return
    if size[pi] < size[pj]:
        pi, pj = pj, pi
    data[pj] = pi
    size[pi] += size[pj]


def connected(ufd, i, j):
    return find(ufd, i) == find(ufd, j)

def ufd_size(ufd, i):
    _, size = ufd
    return size[find(ufd, i)]


################# Miscellanous #################

# product of list
from operator import mul
from functools import reduce
def product(k):
    return reduce(mul, k, 1)


# A
tests = inp()
for _ in range(tests):
    P = inp()
    # code


########## Lazy Sequence ########
# can be bisected
import collections
class LazySequence(collections.Sequence):
    def __init__(self, f, n):
        """Construct a lazy sequence representing map(f, range(n))"""
        self.f = f
        self.n = n
    def __len__(self):
        return self.n
    def __getitem__(self, i):
        if not (0 <= i < self.n):
            raise IndexError
        return self.f(i)