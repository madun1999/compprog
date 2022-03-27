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


# Codeforce 746 Div 2 B
tests = inp()
for _ in range(tests):
    n, x = input_int_gen()
    a = input_list()
    if x <= n // 2:
        print("YES")
    else:
        sorti = sorted(a)
        print("YES" if a[n - x: x] == sorti[n - x: x] else "NO")
