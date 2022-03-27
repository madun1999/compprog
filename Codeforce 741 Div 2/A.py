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


# Codeforce 741 Div 2 A
def f(i, a):
    if a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]
def k(i, a, n):
    if i % 2:
        for t in range(0, n-2, 2):
            f(t, a)
    else:
        for t in range(1, n-1, 2):
            f(t, a)
tests = inp()
for _ in range(tests):
    l, r = input_int_gen()
    if l == r:
        print(0)
    elif l <= (r - 1) // 2 + 1:
        print((r - 1) // 2)
    else:
        print(r - l)
    
