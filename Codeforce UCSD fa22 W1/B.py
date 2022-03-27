from collections import Counter, defaultdict, deque
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


# Codeforce UCSD fa21 W9 B
# from sortedcontainers import SortedList
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    a_sorted = sorted(a)
    counter = Counter(a)
    x = a_sorted[0]
    y = a_sorted[1]
    z = a_sorted[2]
    # print(x,y,z)
    if x != y and y != z:
        print(counter[x] * counter[y] * counter[z])
    elif x == y and y != z:
        print(counter[x]*(counter[x]-1) * counter[z] // 2)
    elif x != y and y == z:
        print(counter[y]*(counter[y]-1) * counter[x] // 2)
    elif x == y == z:
        print((counter[y]*(counter[y]-1) * (counter[y]-2) // 6))

         
        