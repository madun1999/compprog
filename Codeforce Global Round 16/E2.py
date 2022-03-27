from os import write
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

# Codeforces Global Round 16 E
from collections import defaultdict, deque
tests = inp()
for _ in range(tests):
    n = inp()
    children = [set() for _ in range(n+1)]
    # parent = [-1 for _ in range(n+1)]
    bud_dict = [0 for _ in range(n+1)]
    heights = [1 for _ in range(n+1)] # 1 leaf 2 bud
    for _ in range(n-1):
        a, b = input_int_gen()
        children[a].add(b)
        children[b].add(a)
    bfs_queue = deque([(1, 1)])
    while bfs_queue:
        cur, grand = bfs_queue.pop()
        # grand = parent[cur]
        children[cur].discard(grand)
        adjs = children[cur]
        # for adj in adjs:
        #     parent[adj] = cur
        bfs_queue.extendleft([(x, cur) for x in adjs])
    def write_height(i):
        for child in children[i]:
            write_height(child)
            if heights[child] == 1:
                heights[i] = 2
    ############ tree complete ##########

    # write_height(1)
    # using post-order traversal
    # python recursion is expensive (TLE / MLE)

    stk = [(1, False)]
    while stk:
        cur, visited = stk.pop()
        cs = children[cur]
        if not cs:
            continue
        if visited:
            if any(heights[x] == 1 for x in cs):
                heights[cur] = 2
        else:
            stk.append((cur, True))
            stk.extend((x, False) for x in cs)

    n_buds = heights.count(2)
    n_leaves = heights.count(1) - 1
    
    if heights[1] == 2:
        n_buds -= 1
    print(n_leaves - n_buds)



    


