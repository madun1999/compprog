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
    return s[:len(s) - 1]
def input_words():
    return input().split()
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# Kattis 2021 NA Regionals Practice 4
from bisect import bisect_right
tests = 1
for _ in range(tests):
    n,s = input_int_gen()
    d = {}
    l = []
    for _ in range(n):
        nn = input_string()
        name, b = nn.split()
        b = int(b)
        d[b] = name
        l.append(b)
    l.sort()
    ret = []
    idx = len(l)+1
    while s > 0:
        idx = bisect_right(l, s, 0, idx-1)
        if idx == 0:
            ret = []
            s = 0
            break
            
        s -= l[idx-1]
        ret.append(d[l[idx-1]])

    
    print(len(ret))
    if len(ret) > 0:
        print("\n".join(ret))
            