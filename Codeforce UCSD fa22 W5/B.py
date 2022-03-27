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
    n, m = input_int_gen()
    mem = [0 if i == 0 else math.comb(i+m-2, m-1) for i in range(0, n+1)]

    # print(mem)
    sumi = 0
    for i in range(1,n+1):
        for j in range(1, n+2-i):
            sumi = ((mem[i] * mem[j] % MOD) + sumi) % MOD

    print(sumi)

