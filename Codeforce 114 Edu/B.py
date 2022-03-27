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

# Codeforce Educational 114 B
tests = inp()
for _ in range(tests):
    a, b, c, m = input_int_gen()
    maxi = max(a,b,c)
    cut = a + b + c - maxi
    pairs = a + b + c - 3
    mini = max(maxi - 1 - cut, 0)
    print("YES" if pairs >= m >= mini else "NO")
    