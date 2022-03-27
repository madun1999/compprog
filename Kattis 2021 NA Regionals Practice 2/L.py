from bisect import bisect_left, bisect_right
import math
import sys
input = sys.stdin.buffer.readline

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
def input_words():
    return input().split()
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# ICPC NAQ 2021 L
tests = 1
for _ in range(tests):
    n, m = input_int_gen()
    adj = [set() for _ in range(n+1)]
    deg = [0 for _ in range(n+1)]
    edges = []
    for _ in range(m):
        a,b = input_int_gen()
        edges.append((a,b))
        adj[a].add(b)
        adj[b].add(a)
        deg[a] += 1
        deg[b] += 1
    # print(edges, adj)
    
    sumi = 0

    for i in range(1, n+1):
        if deg[i] < 4:
            continue
        csumi = 0
        for j in adj[i]:
            csumi += deg[j] - 1
        sumi += csumi * (deg[i]-1) * (deg[i]-2) * (deg[i]-3) // 6

    tri = 0
    for a,b in edges:
        if deg[b] < deg[a]:
            a,b = b,a 
        for i in adj[a]:
            if i in adj[b] and deg[i] >= 4:
                tri += 1
                sumi -= (deg[i] - 2)*(deg[i] - 3)
    print(sumi)
