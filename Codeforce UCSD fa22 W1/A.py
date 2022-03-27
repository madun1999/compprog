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


import bisect
def t(m):
    arra = [x*(x-1)/2 for x in range(10**5)]
    return bisect.bisect_left(arra, m)

# Codeforce UCSD fa22 W2 A
tests = 1
for _ in range(tests):
    n = inp()
    a = input_list()
    a_sorted = sorted(a)
    re = []
    def swap(rank, idx):
        temp = a[rank]
        a[rank] = a[idx]
        a[idx] = temp
        re.append((rank, idx))
    for rank, x in enumerate(a_sorted):
        idx = a.index(x, rank)
        swap(rank, idx)
    print(len(re))
    for a, b in re:
        print(a,b)
