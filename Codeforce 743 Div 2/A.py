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


# Codeforce 743 Div 2 A
tests = inp()
for _ in range(tests):
    n = inp()
    s = input_string()
    s = [int(x) for x in s]
    ret = 0
    for c in s:
        if c != 0:
            ret += 1 + c
    if s[-1] != 0:
        ret -= 1
    print(ret)
    
