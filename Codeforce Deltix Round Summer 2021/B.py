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


# Codeforce Deltix Round Summer 2021 B
from collections import Counter
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    odd_count = len([x for x in a if x % 2 == 1])
    even_count = n-odd_count
    if not (odd_count - even_count == 1) and not (odd_count - even_count == -1) and not (odd_count - even_count == 0):
        print(-1)
        continue
    ret = 0
    pos = 0
    if odd_count > even_count:
        for i, x in enumerate(a):
            if x % 2 == 1:
                ret += abs(i - pos)
                pos += 2
    elif even_count > odd_count:
        for i, x in enumerate(a):
            if x % 2 == 0:
                ret += abs(i - pos)
                pos += 2
    else:
        reteven = 0
        retodd = 0
        poseven = 0
        posodd = 0
        for i, x in enumerate(a):
            if x % 2 == 1:
                retodd += abs(i - posodd)
                posodd += 2
            if x % 2 == 0:
                reteven += abs(i - poseven)
                poseven += 2
        ret = min(reteven, retodd)
    print(ret)

