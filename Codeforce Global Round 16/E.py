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
    children = defaultdict(set)
    parent = defaultdict(lambda:-1)
    bud_dict = defaultdict(lambda:0)
    heights = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a, b = input_int_gen()
        children[a].add(b)
        children[b].add(a)
    bfs_queue = deque([1])
    while bfs_queue:
        cur = bfs_queue.pop()
        grand = parent[cur]
        children[cur].discard(grand)
        adjs = children[cur]
        for adj in adjs:
            parent[adj] = cur
        bfs_queue.extendleft(adjs)
    def write_height(i):
        for child in children[i]:
            write_height(child)
            if heights[child] != 0:
                bud_dict[i] += 1
        if parent[i] == -1:
            heights[i] = 100000
        else:
            heights[i] = max((heights[child] for child in children[i]), default=-1) + 1
    ############ tree complete ##########
    n_buds = 0
    n_leaves = 0
    write_height(1)
    if 1 in heights:
        visiting = deque([i for i, j in enumerate(heights) if j == 1])
    else:
        visiting = deque()
    def bud(i):
        return i != 1 and children[i] and bud_dict[i] == 0
    while visiting:
        t = visiting.pop()
        if not bud(t):
            continue
        grand = parent[t]
        if grand != -1:
            children[grand].remove(t)
            great_grand = parent[grand]
            bud_dict[grand] -= 1
            if great_grand != -1 and not children[grand]:
                bud_dict[great_grand] -= 1
                if bud_dict[great_grand] == 0:
                    visiting.appendleft(great_grand)
            if bud_dict[grand] == 0 and children[grand]:
                visiting.appendleft(grand)
        # print(t,heights, len(children[t]))
        n_buds += 1
        n_leaves += len(children[t])
    n_leaves += len(children[1]) if children[1] else 1
    # print(children[1], n_leaves, n_buds)
    print(n_leaves - n_buds)



    


