from collections import Counter, deque
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


# Codeforce UCSD fa21 W8 B

tests = inp()
for _ in range(tests):
    n = inp()
    s = input_string()
    # print(s)
    ret = 10
    for i, c in enumerate(s):
        if c == "a":
            # print(i, s)
            if i < n - 1 and s[i+1] == "a":
                ret = 2
                break
            if i < n - 2 and s[i+2] == "a":
                ret = min(ret, 3)
            if i < n - 3 and s[i+3] == "a":
                counter = Counter(s[i:i+4])
                if counter["a"] > counter["b"] and counter["a"] > counter["c"]:
                    ret = min(ret,4)
            # print(i, n, s)
            if i < n - 6 and s[i+6] == "a":
                counter = Counter(s[i:i+7])
                if counter["a"] > counter["b"] and counter["a"] > counter["c"]:
                    ret = min(ret,7)
    print(-1 if ret == 10 else ret)
         
        