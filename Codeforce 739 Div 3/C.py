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


# Codeforce 739 Div 3 C
from math import sqrt
tests = inp()
for _ in range(tests):
    k = inp()
    layer = int(sqrt(k-1))
    rem = k - layer * layer
    if rem > layer + 1:
        print(layer+1, layer - rem + layer + 2)
    else:
        print(rem, layer+1)