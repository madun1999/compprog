from collections import defaultdict
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input().split()
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

# UCSD Fall 21 Week 1 D
tests = 1
for _ in range(tests):
    n = inp()
    if n <= 3:
        print("NO")
    else:
        print("YES")
        if n % 2:
            print("1 + 2 = 3")
            print("5 - 3 = 2")
            print("2 * 3 = 6")
            print("4 * 6 = 24")
            while n > 5:
                print(f"{n} - {n-1} = 1")
                print("24 * 1 = 24")
                n -= 2
        else:
            print("1 * 2 = 2")
            print("2 * 3 = 6")
            print("6 * 4 = 24")
            while n > 4:
                print(f"{n} - {n-1} = 1")
                print("24 * 1 = 24")
                n -= 2