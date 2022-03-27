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
def invr():
    # integer generator 
    return map(int,input().split())


# Codeforce 736 Div 2 A

tests = inp()
for _ in range(tests):
    P = inp()
    dicts = dict()
    for i in range(2, P):
        if P % i in dicts:
            print(dicts[P % i], i)
            break
        else:
            dicts[P % i] = i