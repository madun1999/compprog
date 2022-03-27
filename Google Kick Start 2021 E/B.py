import sys
from types import DynamicClassAttribute
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
# Question 2 Birthday Cake
from collections import Counter, defaultdict
tests = inp()
for test in range(tests):
    R, C, K  = input_int_gen()
    r1, c1, r2, c2 = input_int_gen()

    dr = r2 - r1 + 1
    dc = c2 - c1 + 1


    # for Test Set 1
    # init_cuts = min(r1 - 1, R - r2, c1 - 1, C - c2)
    # h_lines = dr + 1 - (1 if r1 == 1 else 0) - (1 if r2 == R else 0)
    # c_lines = dc + 1 - (1 if c1 == 1 else 0) - (1 if c2 == C else 0)
    # h_cuts = h_lines * (dc) # number of cuts * length of cuts
    # c_cuts = c_lines * (dr) # number of cuts * length of cuts
    # ret = init_cuts + h_cuts + c_cuts
    # print(init_cuts, h_lines, c_lines, dc, dr, h_cuts, c_cuts)

    # for Test Set 2
    rside = (1 if r1 == 1 else 0) + (1 if r2 == R else 0)
    cside = (1 if c1 == 1 else 0) + (1 if c2 == C else 0)
    drr, dcr = dr % K, dc % K
    drb, dcb = dr - drr, dc - dcr
    A = (drb // K)  * (dcb + 1) + dcb * (drb + 1)
    B = drr * (dc // K) + drr * (dcb + 1) 
    D = dcr * (dr // K) + dcr * (drb + 1)

    lowr = min(r1 - 1, R - r2)
    lowc = min(c1 - 1, C - c2)

    E = 

    # ret: minimum number of cuts
    print(f"Case #{test+1}:", ret)