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


# Codeforce 747 Div 2 A
tests = inp()
for _ in range(tests):
    n = inp()
    print(-n + 1, n)
    # if n == 1:
    #     print(0, 1)
    # elif n % 2 == 1:
    #     print(n // 2, n // 2 + 1)
    # else:
    #     print(-n+1, n)