from bisect import bisect_left, bisect_right
import math
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
def input_words():
    return input().split()
def input_int_gen():
    # integer generator 
    return map(int,input().split())


# ICPC NAQ 2021 L
bases = [1, 5, 12, 27, 58, 121, 248, 503, 1014, 2037, 4084, 
            8179, 16370, 32753, 65520, 131055, 262126, 524269, 1048556, 2097131, 4194282]
first_bases = [1] + list(2 ** x for x in range(2, 22))
tests = 1
for _ in range(tests):
    n = inp()
    a = list(reversed(input_list()))
    res_all = []
    pluses = 0
    for ii, i in enumerate(a):
        if ii > 0 and a[ii] == a[ii-1]:
            res_all.insert(-1,"d")
            continue
        res = []
        i += pluses
        while i > 0:
            if not res:
                idx = bisect_right(first_bases, i)-1
                i -= first_bases[idx]
                if idx == 0:
                    res.append("1")
                else:
                    k = idx 
                    res.append("11" + "+d" * k + "+")
                    pluses += k+1
            else:
                idx = bisect_right(bases, i)-1
                i -= bases[idx]
                if idx == 0:
                    res.append("1+")
                    pluses += 1
                else:
                    k = idx + 2
                    res.append("11" + "+d" * (k-1) + "++")
                    pluses += k+1
        res_all.append("".join(res))

    print("".join(reversed(res_all)))