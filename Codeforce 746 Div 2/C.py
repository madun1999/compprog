from collections import defaultdict
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
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# Codeforce 746 Div 2 C
from functools import reduce
tests = inp()
for _ in range(tests):
    n, k = input_int_gen()
    a = input_list()
    edges = defaultdict(set)
    for _ in range(n-1):
        u, v = input_int_gen()
        edges[u-1].add(v-1)
        edges[v-1].add(u-1)
    root = 0
    target = reduce(lambda x, y : x ^ y, a, 0)
    stk = [(0, False, -1)]
    xors = [0 for _ in range(n)] # (subtree xor, parent id)
    parents = [0 for _ in range(n)]
    counts = [0 for _ in range(n)]
    while stk:
        node, visited, par = stk.pop()
        # print(node, visited, par)
        if visited:
            xors[node] = a[node] ^ reduce(lambda x, y : x ^ y, [xors[t] for t in edges[node] if t != par], 0)
            if xors[node] == target:
                xors[node] = 0
                counts[node] += 1
            parents[node] = par
            sub_counts = sum(counts[t] for t in edges[node] if t != par) 
            counts[node] += sub_counts
        else:
            stk.append((node, True, par))
            for x in edges[node]:
                if x != par:
                    stk.append((x, False, node))
    # print(target, xors, a)

    if target == 0:
        print("YES")
    else:
        if k == 2:
            print("NO")
            continue
        else:
            print("YES" if counts[0] >= 3 else "NO")
            continue