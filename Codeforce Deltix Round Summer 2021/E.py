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

def list_to_string(s):
    return ''.join(s)

def flip(a, i, ret):
    a[:i] = a[:i][::-1]
    ret.append(i)
    return a

# Codeforce Deltix Round Summer 2021 E
from collections import Counter
from math import log
tests = 1
for _ in range(tests):
    n, q = input_int_gen()
    a = input_list()
    b = input_list()
    array_all = [x - y for x, y in zip(a, b)]
    p_s = [0]
    for num in array_all:
        p_s.append(p_s[-1] + num)
    
    block_len = int(log(n) / 4)
    min_blocks = []
    max_blocks = []
    temp = 0
    for num in p_s:
        if temp == 0:
            min_blocks.append(num)
            max_blocks.append(num)
        else:
            min_blocks[-1] = min(min_blocks[-1], num)
            max_blocks[-1] = min(max_blocks[-1], num)
        temp = (temp + 1) % block_len

    for _ in range(q):
        l, r = input_int_gen()
        l_sum = p_s[l-1]
        mini = 1
        if p_s[r] != l_sum:
            print(-1)
            continue

        mini = min(p_s[l:r]) - l_sum
        maxi = max(p_s[l:r]) - l_sum
        if maxi > 0:
            print(-1)
        else:
            print(-mini)