
import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input()[:-1].split()
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
 
# ICPC NAQ 2021 E
from collections import defaultdict
tests = 1
for _ in range(tests):
    s = input_string()
    pre = 0
    left = True
    for i in s:
        if i == "|":
            pre += (1 if left else -1)
        if i == "(":
            left = False
    print("fix" if pre else "correct")
    