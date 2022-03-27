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

# Codeforce 743 Div 2 C
from collections import defaultdict
tests = inp()
for _ in range(tests):
    n = inp()
    edges = defaultdict(set)
    back_edges = dict()
    sources = set()
    distance = [0 for _ in range(n)]
    for i in range(n):
        a = input_list()
        k = a.pop(0)
        for c in a:
            edges[c-1].add(i)
        if k == 0:
            sources.add(i)
        back_edges[i] = set(x-1 for x in a)
        
    visited = [False for _ in range(n+1)]
    visited_temp = [False for _ in range(n+1)]
    # topological sort
    stk = [(l, False) for l in range(n)]
    res = []
    while stk:
        i, state = stk.pop()
        if state:
            res.append(i)
            visited_temp[i] = False
            visited[i] = True
        else:
            if visited[i]:
                continue
            if visited_temp[i]:
                print(-1)
                break
            visited_temp[i] = True
            stk.append((i, True))
            for child in edges[i]:
                stk.append((child, False))
    else:
        # res.pop()
        res.reverse()
        print(res)
        if len(res) != n:
            print(-1)
            continue
        understood = set()
        nexts = set()
        layers = 0
        for c in res:
            if back_edges[c].issubset(understood):
                nexts.add(c)
            else:
                layers += 1
                understood |= nexts
                understood.add(c)
                nexts = set()
        print(layers)
    
