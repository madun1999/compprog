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

mem = [0]
def xors(n):
    if len(mem) > n:
        return mem[n]
    else:
        for i in range(len(mem), n+1):
            mem.append(mem[-1] ^ i)
        return mem[n]

# Codeforce 742 Div 2 B
tests = inp()
for _ in range(tests):
    a, b = input_int_gen()
    x = xors(a-1)
    if x == b:
        print(a)
    elif x == b ^ a:
        print(a + 2)
    else:
        print(a + 1)