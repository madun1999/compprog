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


# Codeforce 739 Div 3 B
tests = inp()
for _ in range(tests):
    a,b,c  = input_int_gen()
    halfsize = abs(a-b)
    size = halfsize * 2
    d = c + halfsize if c <= halfsize else c - halfsize
    if a > size or b > size or c > size:
        print(-1)
    else:
        print(d)