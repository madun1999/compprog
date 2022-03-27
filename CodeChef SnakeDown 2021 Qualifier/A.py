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
def print_bool(s):
    print("YES" if s else "NO")

# LUCKYNUM
tests = inp()
for _ in range(tests):
    a = input_list()
    print_bool(any(x == 7 for x in a))
