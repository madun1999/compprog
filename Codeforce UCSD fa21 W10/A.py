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


import bisect
def t(m):
    arra = [x*(x-1)/2 for x in range(10**5)]
    return bisect.bisect_left(arra, m)

# Codeforce UCSD fa21 W9 A
tests = 1
for _ in range(tests):
    n,m = input_int_gen()
    print(max(0, n-2*m), n if m == 0 else n-t(m))
    