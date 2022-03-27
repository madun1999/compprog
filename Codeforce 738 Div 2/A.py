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


# Codeforce 738 Div 2 A

tests = inp()
for _ in range(tests):
    n = inp()
    # code here
    a = input_list()
    ret = a[0]
    for x in a:
        ret &= x
    print(ret)