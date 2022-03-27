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


# Codeforce 736 Div 2 B
from math import gcd
from itertools import combinations
no_fences = inp()
fences = []
for _ in range(no_fences):
    a, b  = input_int_gen()
    fences.append((a,b))

def boudnary_count(a,b):
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        return abs(y1 - y2) - 1
    if y1 == y2:
        return abs(x1 - x2) - 1
    return gcd(abs(x1 - x2), abs(y1 - y2)) - 1

interesting = 0
for a,b,c in combinations(fences, 3):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    double_area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    bound = boudnary_count(a,b) + boudnary_count(b,c) + boudnary_count(a,c) + 3
    points = (double_area - bound + 2) // 2
    if points % 2 == 1:
        interesting += 1
print(interesting)
