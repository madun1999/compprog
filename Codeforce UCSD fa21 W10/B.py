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


# Codeforce UCSD fa21 W9 B
# from sortedcontainers import SortedList
tests = 1
for _ in range(tests):
    n,m,s,t = input_int_gen()
    edges = defaultdict(set)
    for _ in range(m):
        u,v = input_int_gen()
        edges[u].add(v)
        edges[v].add(u)

    l = [s]
    visited = {s}
    layer = 0
    dist_to_s = {s:0}
    while l:
        layer += 1
        new_l = []
        for x in l:
            for y in edges[x]:
                if y not in visited:
                    new_l.append(y)
                    visited.add(y)
                    dist_to_s[y] = layer
        l = new_l

    l = [t]
    visited = {t}
    layer = 0
    dist_to_t = {t:0}
    while l:
        layer += 1
        new_l = []
        for x in l:
            for y in edges[x]:
                if y not in visited:
                    new_l.append(y)
                    visited.add(y)
                    dist_to_t[y] = layer
        l = new_l
    # print(layer)
    # print(edges)
    # print(visited)
    # print(dist_to_s)
    # print(dist_to_t)
    s_t_dist = dist_to_t[s]

    ret = 0
    for x in range(1,n+1):
        for y in range(1,n+1):
            if x < y and y not in edges[x]:
                if dist_to_s[x] + 1 + dist_to_t[y] >= s_t_dist and dist_to_t[x] + 1 + dist_to_s[y] >= s_t_dist:
                    ret += 1
    print(ret)


    
         
        