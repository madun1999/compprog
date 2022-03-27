from collections import defaultdict
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


from sortedcontainers import SortedList
# Codeforce UCSD fa22 W6 G
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    seen = SortedList()
    score = 0
    # print(n, a, seen)
    for i in a:
        idx = seen.bisect(i)
        if idx == 0:
            lower = 0
        else:
            lower = seen[idx-1]
        if idx >= len(seen):
            upper = n+1
        else:
            upper = seen[idx]
        score += upper - lower - 1
        # print(upper, lower, upper - lower - 1)
        seen.add(i)
    print(score)

