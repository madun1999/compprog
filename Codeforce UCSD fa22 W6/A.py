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
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())


# import bisect
# def t(m):
#     arra = [x*(x-1)/2 for x in range(10**5)]
#     return bisect.bisect_left(arra, m)

# Codeforce UCSD fa22 W6 A
# tests = inp()
tests = 1
for _ in range(tests):
    n = inp()
    a = []
    for _ in range(n):
        a.append(''.join(input_string()))
    print('\n'.join(x for x in list(reversed(a))))