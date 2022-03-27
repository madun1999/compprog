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


# UCSD Fall 21 Week 5 B
tests = 1
for _ in range(tests):
    n = inp()
    s = input_string()
    a = input_list()

    s = [int(x) for x in s]
    sc = []
    count = 0
    last = s[0]

    mem = [[[[0 for _ in range(2)] for _ in range(n+1)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mem[0][0][1][s[i]] = a[1-1]
    for i in range(n):
        for j in range(n):
            if i >= j: continue
            for t in range(n):
                if t > j - i + 1: continue
                for t2 in range(n):
                    if s[i] == s[j]:
                        mem[i][j][t2+2][s[i]] =  mem[i][j][t2][s[i]] - maxcons[t2] + maxcons[t2+2]
                        mem[i][j][t2][1 - s[i]] = mem[i][j][t2][1 - s[i]] + 
                    else:
                        mem[i][j][t2+1][s[i]] =  mem[i][j][t2][s[i]]
                        mem[i][j][t2+1][s[j]] =  mem[i][j][t2][s[j]] 

    print(mem[-1])
    

