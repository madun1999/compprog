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

def andor(a, b):
    print("and", a, b)
    sys.stdout.flush()
    andi = inp()
    print("or", a, b)
    sys.stdout.flush()
    ori = inp()
    return (andi, ori, b)
def sort_andor(and1, or1, and2, or2, and3, or3):
    a = (and1 | and2) | (or2 & ~or3)
    b = (and2 | and3) | (or3 & ~or1)
    c = (and3 | and1) | (or1 & ~or2)
    return sorted([a,b,c])
# Codeforce Deltix Round Summer 2021 D
tests = 1
for _ in range(tests):
    x = input_int_gen()
    if x == -1:
        break
    n, k = x
    res = []
    for idx in range(n-1):
        res.append(andor(1, idx+2))
    res.sort(key=lambda x: (x[1] + x[0]))
    if k == 1:
        andis1, oris1, idxs1 = res[0]
        andis2, oris2, idxs2 = res[1]
        andia, oria, _ = andor(idxs2, idxs1)
        print("finish", sort_andor(andis1, oris1, andis2, oris2, andia, oria)[0])
    elif k == n:
        andis1, oris1, idxs1 = res[-2]
        andis2, oris2, idxs2 = res[-1]
        andia, oria, _ = andor(idxs2, idxs1)
        print("finish", sort_andor(andis1, oris1, andis2, oris2, andia, oria)[2])
    else:
        andis1, oris1, idxs1 = res[k-2]
        andis2, oris2, idxs2 = res[k-1]
        andia, oria, _ = andor(idxs2, idxs1)
        print("finish", sort_andor(andis1, oris1, andis2, oris2, andia, oria)[1])
