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

# UCSD Fall 21 Week 1 B
from collections import Counter
tests = 1
for _ in range(tests):
    n = inp() 
    a = input_list()
    par = [x % 2 for x in a]
    par_counter = Counter(par)
    if par_counter[1] == 1:
        print(par.index(1) + 1)
    else:
        print(par.index(0) + 1)
