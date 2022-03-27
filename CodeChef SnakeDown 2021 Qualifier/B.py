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
def print_bool(s):
    print("YES" if s else "NO")

# TESTSERIES
tests = inp()
for _ in range(tests):
    a = input_list()
    india = a.count(1)
    england = a.count(2)
    print("DRAW" if india == england else ("india" if india > england else "england"))
