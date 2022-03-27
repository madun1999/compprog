from bisect import bisect_left, bisect_right
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
def input_words():
    return input().split()
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# ICPC NAQ 2021 I
tests = 1
for _ in range(tests):
    n = inp()
    conds = []
    ing = set()
    for _ in range(n):
        ws = input_words()
        # print(ws)
        if len(ws) == 1:
            ing.add(ws[0])
        else:
            cond_post = ws[-1]
            cond_pre = set(ws[i] for i in range(1, len(ws) - 2, 2) if ws[i])
            cond_adj = ws[2]
            if ws[2] == "then": 
                cond_adj = "or"
            conds.append((cond_pre, cond_post, cond_adj, False))
    # print(conds)
    for _ in conds:
        for idx, (cond_pre, cond_post, cond_adj, sat) in enumerate(conds):
            if sat: 
                continue
            if cond_adj == "or":
                for i in cond_pre:
                    if i in ing:
                        ing.add(cond_post)
                        conds[idx] = (0,0,0,True)
                        break
            if cond_adj == "and":
                new_red = set()
                for i in cond_pre:
                    if i in ing:
                        new_red.add(i)
                    else:
                        break
                cond_pre -= new_red
                if not cond_pre:
                    ing.add(cond_post)
                    conds[idx] = (0,0,0,True)

    print(len(ing))
            