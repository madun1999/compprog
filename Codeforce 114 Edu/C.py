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

# Codeforce Educational 114 C
from collections import defaultdict
from bisect import bisect_left
# tests = inp()
tests = 1
res = []
for _ in range(tests):
    n = inp() 
    a = input_list()
    a.sort()
    sumi = sum(a)
    m = inp()
    for _ in range(m):
        defense, attack = input_int_gen()
        i = bisect_left(a, defense)
        inc_defense = sumi + defense + attack
        inc_attack = sumi + attack + defense
        if i < n:
            inc_defense = max(0, defense - a[i]) + max(attack - (sumi - a[i]), 0)
        i -= 1
        if i >= 0:
            inc_attack = max(0, defense - a[i]) + max(attack - (sumi - a[i]), 0)
        print(str(min(inc_defense, inc_attack)))
#         res.append(str(min(inc_defense, inc_attack)))
# print("\n".join(res))
            

            