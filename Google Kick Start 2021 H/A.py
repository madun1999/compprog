import sys
input = sys.stdin.buffer.readline

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


# Google Kick Start 2021 H Problem A
from collections import Counter

tests = inp()
for test in range(tests):
    s = input_string()
    alpha = set(input_string())
    s_counter = Counter(s)
    sumi = 0
    # print(alpha)
    for c, count in s_counter.items():
        mini = 30

        for target in alpha:
            t = target
            a = c
            
            mini = min(mini, abs(t - a), 26 - abs(t - a))
        sumi += mini * count

    print(f"Case #{test+1}:", sumi)