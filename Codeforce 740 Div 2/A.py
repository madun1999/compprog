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


# Codeforce 740 Div 2 A
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
    n = inp()
    a = input_list()
    a_sorted = sorted(a)
    if a == a_sorted:
        print(0)
        continue
    ret = 0
    while a != a_sorted:
        ret += 1
        k(ret, a, n)
    print(ret)
