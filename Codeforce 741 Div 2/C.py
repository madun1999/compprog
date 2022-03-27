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


# Codeforce 741 Div 2 C
from math import sqrt
tests = inp()
for _ in range(tests):
    n = inp()
    s = input_string()
    s = [int(k) for k in s]
    for i, k in enumerate(s[n // 2: ]):
        if k == 0:
            print(1,n // 2 + 1 + i,1,n // 2 + i)
            break
    else:
        for i in range(n // 2 - 1, -1, -1):
            k = s[i]
            if k == 0:
                print(i+1, n, i+2, n)
                break
        else:
            print(1, n//2, n-n//2+1, n)