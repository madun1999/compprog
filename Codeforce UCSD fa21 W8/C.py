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

# Codeforce UCSD fa21 W8 C
# from collections import Counter
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    up = False
    ls = [a[0]]
    last = a[1]
    i = 0
    while i < n and a[i] == a[i+1]:
        i += 1
    i += 1
    up = ls[-1] < a[i]
    last = a[i]
    # print(f"{i=} {up=}")
    for t in a[i+1:]:
        if last < t and not up:
            ls.append(last)
            # last = t
            up = True 
        if last > t and up:
            ls.append(last)
            # last = t
            up = False
        last = t
    ls.append(a[-1])
    print(len(ls))
    print(" ".join((str(x) for x in ls)))