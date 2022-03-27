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

# Codeforce 742 Div 2 C
from collections import Counter
MOD = 998_244_353
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    maxi = max(a)
    c = Counter(a)
    upper = c[maxi]
    if upper >= 2:
        # factorial
        prodi = 1
        for i in range(2,n+1):
            prodi = (prodi * i) % MOD
        print(prodi)

    else:
        lower = c[maxi - 1]
        if lower < 1:
            print(0)
        else:
            # at least one lower after the upper
            prodi = 1
            for i in range(2,n+1):
                if i == lower + 1:
                    continue
                prodi = (prodi * i) % MOD
            print((prodi * lower) % MOD)
