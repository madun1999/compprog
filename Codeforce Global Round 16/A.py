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


# Codeforces Global Round 16 A
tests = inp()
for _ in range(tests):
    s, n = input_int_gen()
    m = s // 2 + 1
    k = n % m
    print(n // m)
    
