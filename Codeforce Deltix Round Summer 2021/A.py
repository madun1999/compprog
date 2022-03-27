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


# Codeforce Deltix Round Summer 2021 A
tests = inp()
for _ in range(tests):
    l, r = input_int_gen()
    if l == 0 and r == 0:
        print(0)
    elif (l + r) % 2 != 0:
        print(-1)
    elif l == r:
        print(1)
    else:
        print(2)
    
