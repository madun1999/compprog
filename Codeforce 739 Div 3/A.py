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


# Codeforce 739 Div 3 A

tests = inp()
for _ in range(tests):
    n = inp()
    a = [x for x in range(3000) if x % 10 != 3 and x % 3 != 0]
    print(a[n-1])