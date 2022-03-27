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
    back_edges = defaultdict(set)
    for i in range(n):
        i += 1
        a = input_list()
        k = a.pop(0)
        for c in a:
            edges[c].add(i)
        back_edges[i] = set(a)
    understood = set()
    check = set()
    # first pass
    for i in range(1, n+1):
        if back_edges[i].issubset(understood):
            understood.add(i)
            check |= edges[i]
    check -= understood
    # more passes
    passes = 1
    while check:
        passes += 1
        check = sorted(check)
        new_check = set()
        for c in check:
            if back_edges[c].issubset(understood):
                understood.add(c)
                new_check |= edges[c]
        new_check -= understood
        check = new_check
    if len(understood) < n:
        print(-1)
    else:
        print(passes)
