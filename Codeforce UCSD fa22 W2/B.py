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


# Codeforce UCSD fa22 W2 B
# from sortedcontainers import SortedList
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    or_sum = 0
    twice_sum = 0
    for k in a:
        twice_sum = twice_sum | or_sum & k
        or_sum |= k
    maxi = -1
    result = 0
    for k in a:
        remain = (or_sum - k) | twice_sum
        if (k & (~remain)) > maxi:
            maxi = k & (~remain)
            result = k
    out_l = [result]
    en = False
    for k in a:
        if not en and k == result:
            en = True
        else:
            out_l.append(k)
    print(" ".join(str(t) for t in out_l))