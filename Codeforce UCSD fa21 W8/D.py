from collections import Counter, defaultdict
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input().split()
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

# Codeforce UCSD fa21 W8 D
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    mem = defaultdict(int)
    sumi = 0
    for c in a:
        new_mem = defaultdict(int)
        for prev, val in mem.items():
            cur = c - prev
            if cur == 0:
                sumi += val
                # continue
            if cur >= 0:
                new_mem[cur] = val
        new_mem[c] += 1
        if c == 0:
            sumi += 1
        mem = new_mem
        # print(mem)
    print(sumi)
        