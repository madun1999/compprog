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

# Google Kick Start 2021 H Problem C
from collections import Counter
tests = inp()
for test in range(tests):
    n = inp() 
    a = input_string()
    k = []
    for d in a:
        d = int(d)
        while d != -1:
            if k and (k[-1] + 1) % 10 == d:
                del k[-1] 
                d = (d + 1) % 10
            else:
                k.append(d)
                d = -1
    
    print(f"Case #{test+1}:", "".join([str(x) for x in k]))