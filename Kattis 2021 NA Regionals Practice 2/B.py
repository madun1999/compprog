from collections import Counter, defaultdict, deque
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


# Kattis 2021 NA Regionals Practice 2
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
   