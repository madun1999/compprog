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

# Codeforce 747 Div 2 C
tests = inp()
for _ in range(tests):
    input_temp = input_string()
    l = input_temp.split()
    n, c = int(l[0]), l[1]
    s = input_string()
    
    # n, c, s
    # print(n,c,s)
    if s == c * n:
        print(0)
        continue

    try:
        idx = s.index(c, n // 2)
        print(1)
        print(idx + 1)
    except ValueError:
        print(2)
        print(n, n-1)
