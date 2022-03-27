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


# Google Kick Start 2021 Round E 
# Question 4 Increasing Sequence Card Game
from collections import Counter, defaultdict
tests = inp()
for test in range(tests):
    R, C, K  = input_int_gen()
    r1, c1, r2, c2 = input_int_gen()

    dr = r2 - r1 + 1
    dc = c2 - c1 + 1

    if dr > dc:
        R, C = C, R
        dr, dc = dc, dr
        r1, c1 = c1, r1
        r2, c2 = c2, r2

    # for Test Set 1
    init_cuts = min(r1 - 1, R - r2, c1 - 1, C - r2)
    h_lines = dr + 1 - (1 if r1 == 1 else 0) - (1 if r2 == R else 0)
    c_lines = dc + 1 - (1 if c1 == 1 else 0) - (1 if c2 == C else 0)
    h_cuts = h_lines * (dc) # number of cuts * length of cuts
    c_cuts = c_lines * (dr) # number of cuts * length of cuts
    ret = init_cuts + h_cuts + c_cuts
    print(init_cuts, h_lines, c_lines, dc, dr, h_cuts, c_cuts)

    # for Test Set 2

    # h_lines = dr + 1 - (1 if r1 == 1 else 0) - (1 if r2 == R else 0)
    # c_lines = dc + 1 - (1 if c1 == 1 else 0) - (1 if c2 == C else 0)
    # h_cuts = (dc + K - 1) // K
    # c_cuts = (dr + K - 1) // K
    # h_tcuts = h_lines * (dc) # number of cuts * length of cuts
    # c_tcuts = c_lines * (dr) # number of cuts * length of cuts
    # init_cuts = min(r1 - 1, R - r2, c1 - 1, C - r2)
    # ret = init_cuts + h_cuts + c_cuts

    # ret: minimum number of cuts
    print(f"Case #{test+1}:", ret)