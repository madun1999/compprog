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


# Codeforce Educational 114 A
tests = inp()
for _ in range(tests):
    n = inp()
    for i in range(n):
        a = i
        b = n - i
        print("(" * a + ")" * a + "(" * b + ")" * b)
    
    
