# from collections import Counter, defaultdict, deque
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


import math 
MOD = 10 ** 9 + 7

def combmod(a, b):
    prodi = 1
    for i in range(b):
        prodi = prodi * (a - i) % MOD
    return prodi 

# Codeforce UCSD fa22 W6 B
# from sortedcontainers import SortedList
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    a.append(0)
    area = 0
    a.sort(reverse=True)
    for i in range(n):
        if i % 2 == 0:
            area += (a[i] ** 2 - a[i+1] ** 2) * math.pi
    print(area)