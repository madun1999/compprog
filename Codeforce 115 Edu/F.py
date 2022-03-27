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
    s = input().decode()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# Codeforce 115 Edu F
from itertools import permutations
tests = 1
for _ in range(tests):
    n = inp()
    a = []
    for _ in range(n):
        a.append(input_string())
    maxi = 0
    for l in permutations(a,len(a)):
        print(l)
        s = "".join(l)
        left = 0
        right = 0
        bracs = 0
        freeze = False
        for c in s:
            if c == "(":
                left += 1
            if c == ")":
                if left:
                    left -= 1
                    if not left and not freeze:
                        bracs += 1
                else:
                    right += 1
                    freeze = True
                    break
        maxi = max(maxi, bracs)
    print(maxi)