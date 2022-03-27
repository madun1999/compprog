
import sys
input = sys.stdin.buffer.readline
 
############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input()[:-1].split()
def input_list():
    # list of integers
    return list(map(int,input().split()))
def input_string():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().decode().split())
 
# Codeforce 115 Edu E
from collections import defaultdict
from sortedcontainers import SortedList
tests = inp()
for _ in range(tests):
    n, m, q = input_int_gen()
    corners = [True, True] 
    black = defaultdict(SortedList()) # for _ in range((m + n - 1))
    blue = defaultdict(SortedList()) # for _ in range((m + n - 1))
    for i in range(-n+1, m):
        black[i].add(min(2 * (n + i) + 1, 2 * (m - i)))
        blue[m + n - 1 - i].add()
    for _ in range(q):
        x, y = input_int_gen()
        # blue (horizontal first)
        i = 1
        if (x,y) in k[i]: k[i].remove((x,y))
        else: k[i].add((x,y))
        i = 2
        if (x,y) in k[i]: k[i].remove((x,y))
        else: k[i].add((x,y))
        # black (vertical first)
        i = 3
        if (x,y) in k[i]: k[i].remove((x,y))
        else: k[i].add((x,y))
        i = 4
        if (x,y) in k[i]: k[i].remove((x,y))
        else: k[i].add((x,y))