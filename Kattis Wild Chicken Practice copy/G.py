from bisect import bisect_left, bisect_right
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
def input_words():
    return input().split()
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# ICPC NAQ 2021 G
tests = 1
for _ in range(tests):
    C,N = input_int_gen()
    a = input_list()
    current = 1
    correct = []
    error = []
    idx = 0
    while idx < N:
        i = a[idx]
        if current != i:
            if i - current == 1:
                correct.append(str(current))
            else:
                correct.append(str(current) + "-" + str(i-1))
            current = i
        while idx+1 < N and i+1 == a[idx+1]:
            idx += 1
            i = a[idx]
        if i == current:
            error.append(str(current))
        else:
            error.append(str(current) + "-" + str(i))
        current = i+1
        idx += 1
    # print(current, C)
    if current == C:
        correct.append(str(current))
    elif current < C:
        correct.append(str(current) + "-" + str(C))
    
    print("Errors: " + ", ".join(error[:-1]) + " and " + error[-1])
    print("Correct: " + ", ".join(correct[:-1]) + " and " + correct[-1])