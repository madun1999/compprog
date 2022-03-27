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


# Codeforce 115 Edu A
tests = inp()
for _ in range(tests):
    n = inp()
    a1 = input_string()
    a2 = input_string()
    for s1, s2 in zip(a1, a2):
        if s1 == s2 == "1":
            print("NO")
            break
    else:
        print("YES")