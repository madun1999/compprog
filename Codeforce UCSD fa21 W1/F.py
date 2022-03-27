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

# Codeforce 747 Div 2 F
tests = inp()
for _ in range(tests):
    s, n, k  = input_int_gen()
    q = (s+1) // k
    r = (s+1) % k
    maxi = r * ((q+2) // 2) + (k-r) * ((q+1) // 2)
    print("YES" if maxi < n + 1 else "NO")

