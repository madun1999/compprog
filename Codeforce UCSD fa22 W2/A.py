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


# import bisect
# def t(m):
#     arra = [x*(x-1)/2 for x in range(10**5)]
#     return bisect.bisect_left(arra, m)

# Codeforce UCSD fa22 W2 A
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_string()
    l = 0
    r = 0
    for i in a:
        if i == ">":
            break
        l += 1
    
    for i in reversed(a):
        if i == "<":
            break
        r += 1
    
    print(min(l,r))