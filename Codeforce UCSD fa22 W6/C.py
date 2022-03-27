from collections import defaultdict
import sys
import heapq
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
    
def input_float_gen():
    # float generator 
    return map(float,input().split())
# Codeforce UCSD fa22 W6 C

import math
# tests = inp()
tests = 1
for _ in range(tests):
    n = inp()
    sum = 0
    for _ in range(n):
        a, b = input_float_gen()
        a  = round(math.log2(a/440) * 12)
        b  = round(math.log2(b/440) * 12)
        # print(a, b)
        sum += b-a
    k = sum // n
    rems = [abs(sum - n * k), abs(sum - n * (k+1))]
    # print(sum, n, rems, k)
    print(min(rems))