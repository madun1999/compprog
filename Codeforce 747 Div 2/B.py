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


# Codeforce 747 Div 2 B
MOD = 10 ** 9 + 7
tests = inp()
for _ in range(tests):
    n, k = input_int_gen()
    sumi = 0
    base = 1
    oldn = n
    while k:
        if k % 2 == 1:
            sumi = (sumi + base) % MOD
        k = k // 2
        base = (base * oldn) % MOD
    print(sumi) 
