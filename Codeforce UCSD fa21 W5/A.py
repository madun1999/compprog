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


# UCSD Fall 21 Week 5 A
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    pre = [0]
    for i in range(n-1):
        last = pre[-1]
        t = abs(a[i] - a[i+1]) 
        pre.append(last + t if i % 2 == 0 else last - t)

    # print(pre)

    minipre = 0
    maxi = 0
    for i in range(n):
        maxi = max(maxi, pre[i] - minipre)
        if i % 2 == 0:
            minipre = min(minipre, pre[i])
    # print(maxi)

    maxipre = pre[1]
    for i in range(1, n):
        maxi = max(maxi, maxipre - pre[i])
        if i % 2 == 1:
            maxipre = max(maxipre, pre[i])
    print(maxi)
    