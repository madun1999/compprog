from collections import Counter, defaultdict
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input().split()
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

# Codeforce UCSD fa22 W2 D
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    or_sum = 0
    first_sum = 0
    for k in a:
        second_sum = second_sum | or_sum & k
        or_sum |= k
    print(or_sum - second_sum)
    
    

    