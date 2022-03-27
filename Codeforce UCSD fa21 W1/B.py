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


# UCSD Fall 21 Week 1 B
tests = inp()
for _ in range(tests):
    s = input_string()
    if len(s) <= 10:
        print("".join(s))
    else: 
        print(s[0] + str(len(s) - 2) + s[-1])
