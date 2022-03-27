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

# Codeforces Global Round 16 C
from math import sqrt
tests = inp()
for _ in range(tests):
    length = inp()
    n = input_string()
    m = input_string()
    n = [int(x) for x in n]
    m = [int(x) for x in m]
    n.append(3)
    m.append(3)
    res = 0
    z_pair = False
    o_pair = False
    for i, j in zip(n, m):
        if i == j == 1:
            if z_pair:
                res += 2
                # print("01")
                z_pair = False
            else:
                o_pair = True
        elif i == j == 0:
            if o_pair:
                res += 2
                # print("10")
                o_pair = False
                z_pair = False
            elif z_pair:
                # print("0")
                res += 1
            else:
                z_pair = True
        else:
            if i != 3:
                # print("2")
                res += 2
            if z_pair:
                # print("0'")
                res += 1
                z_pair = False
            o_pair = False
            
    print(res)