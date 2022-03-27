
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

# Codeforce 742 Div 2 D
from bisect import bisect_left
from collections import defaultdict
from math import comb
tests = inp()
for _ in range(tests):
    n, m, k = input_int_gen()
    xs = input_list()
    ys = input_list()
    horis_total = defaultdict(int)
    vertis_total = defaultdict(int)
    horis = defaultdict(lambda: defaultdict(int))
    vertis = defaultdict(lambda: defaultdict(int))
    for _ in range(k):
        a,b = input_int_gen()
        ix = bisect_left(xs, a)
        iy = bisect_left(ys, b)
        if xs[ix] != a:
            horis_total[ix] += 1
            horis[ix][iy] += 1
        elif ys[iy] != b:
            vertis_total[iy] += 1
            vertis[iy][ix] += 1
    # print(horis, vertis)
    res = 0
    for d in horis.values():
        for x in d.values():
            res -= comb(x, 2)
    for d in vertis.values():
        for x in d.values():
            res -= comb(x, 2)
    for c in horis_total.values():
        res += comb(c, 2)
    for c in vertis_total.values():
        res += comb(c, 2)
    print(res) 

        
    
        



