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

def list_to_string(s):
    return ''.join(s)

def flip(a, i, ret):
    a[:i] = a[:i][::-1]
    ret.append(i)
    return a

# Codeforce 740 Div 2 E
from collections import Counter
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    ret = []
    flag = False
    for i, m in enumerate(a):
        if (i+1) % 2 != m % 2:
            flag = True
            print(-1)
            break
    if flag:
        continue
    # print(n)
    for m in range(n, 2, -2):
        odd = a.index(m)
        even = a.index(m-1)
        if odd > even:
            i,j = even+1, odd+1
            flip(a, j, ret)
            flip(a, j-i, ret)
            flip(a, j-i+2, ret)
            flip(a, 3, ret)
            flip(a, m, ret)
        else:
            i,j  = odd+1, even+1
            flip(a, i, ret)
            flip(a, j-1, ret)
            flip(a, j+1, ret)
            flip(a, 3, ret)
            flip(a, m, ret)

    print(len(ret))
    print(' '.join(str(x) for x in ret))
    