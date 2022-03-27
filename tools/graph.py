
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