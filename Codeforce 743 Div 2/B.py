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

# Codeforce 743 Div 2 B
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    b = input_list()
    aa = [0 for _ in a]
    bb = [0 for _ in b]
    for i, (x,y) in enumerate(zip(a,b)):
        aa[a[i] // 2] = i
        bb[b[i] // 2 - 1] = i
    mini = n
    for idx, xx in enumerate(aa):
        mini = min(xx, mini)
        aa[idx] = mini
    # print(aa, bb)
    mini = n * 2
    for idx, y in enumerate(b):
        mini = min(mini, idx + aa[y // 2 - 1])
    print(mini)