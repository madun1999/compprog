
import sys
input = sys.stdin.buffer.readline
 
############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input()[:-1].split()
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
 
# Codeforce UCSD fa22 W6 E
from collections import defaultdict
MOD = 10 ** 9 + 7
tests = 1
for _ in range(tests):
    M, N = input_int_gen()
    beats = input_list()
    M *= 4
    # print(M,N)
    mem = [1]
    for i in range(1, M+1):
        sumi = 0
        for j in beats:
            if j <= i:
                # print(i,j)
                # print(mem, mem[i-j])
                sumi = (mem[i-j] + sumi) % MOD 
        mem.append(sumi)
    # print(mem)
    print(mem[-1])