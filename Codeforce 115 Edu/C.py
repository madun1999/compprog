from collections import defaultdict
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
    # return list(s[:len(s) - 1])
    return s[:-1]
def input_string_l():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# Codeforce 115 Edu C
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    sumi = sum(a)
    target = (sumi * 2) / n
    if (sumi * 2) % n != 0:
        print(0)
        continue
    c = defaultdict(int)
    for i in a:
        c[target - i] += 1
    ret = 0
    k = 0
    for i in a:
        if i == target - i:
            c[i] -= 1
            ret += c[i]
        else:
            if i < target - i:
                ret += c[i]
    print(ret)