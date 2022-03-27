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

def combs(x):
    if x >= 10:
        return 19 - x
    else:
        return x + 1

# Codeforce 742 Div 2 C
from math import sqrt
tests = inp()
for _ in range(tests):
    n = input_string()
    n = [int(x) for x in n]
    length = len(n)
    ret = 0
    for i in range(1 << max(0,length - 2)):
        nc = [x for x in n]
        ii = [int(x) for x in bin(i)[2:]]
        ii = [0] * (length - 2 - len(ii))+ ii
        for idx, x in enumerate(ii):
            if x:
                nc[idx+2] += 10
                nc[idx] -= 1
        
        prod = 1
        minus = 2
        for t in nc:
            if t < 0:
                prod = 0
                minus = 0
                break
            prod *= combs(t)
            if t >= 10:
                minus = 0
        ret += prod - minus
        # print(ii, nc, prod - minus)
    print(ret)