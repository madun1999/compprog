from collections import defaultdict
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
    # return list(s[:len(s) - 1])
    return s[:-1]
def input_string_l():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())

def cost(colors, costs, line):
    total = 0
    color_list = {}
    for i, v in enumerate(line):
        total += costs[colors[i % 3]][v-1]
        color_list[v] = colors[i % 3] + 1
    return total, color_list

# Codeforce UCSD fa21 W9 C
# from collections import Counter
tests = 1
for _ in range(tests):
    n = inp()
    c = [1,2,3]
    c[0] = input_list()
    c[1] = input_list()
    c[2] = input_list()
    edges = defaultdict(set)
    for _ in range(n-1):
        u, v = input_int_gen()
        edges[u].add(v)
        edges[v].add(u)
        if len(edges[u]) > 2 or len(edges[v]) > 2:
            print(-1)
            exit()
    ends = []
    for x in range(1, n+1):
        if len(edges[x]) == 1:
            ends.append(x)
    line = [ends[0], next(iter(edges[ends[0]]))]
    while len(line) < n:
        for v in edges[line[-1]]:
            if v != line[-2]:
                line.append(v)
                break
    # if n == 4:
    #     print(c)
    #     print(edges)
    #     print(line)
    mini = float('inf')
    color_list = 1
    for tup in [(0,1,2), (0,2,1), (2,1,0), (2,0,1), (1,0,2), (1,2,0)]:
        cc, cl = cost(tup, c, line)
        # if n == 4:
        #     print(cc, cl)
        if cc < mini:
            mini = cc
            color_list = cl
    
    print(mini)
    print(" ".join(str(color_list[x]) for x in range(1,n+1)))
        

