import sys
input = sys.stdin.buffer.readline

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


# Codeforce UCSD fa21 W9 A
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    total = max(a) - min(a) + 1
    print(total - n)
    