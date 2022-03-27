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


# Codeforce 741 Div 2 B
from collections import Counter
tests = inp()
for _ in range(tests):
    n = inp()
    s = input_string()
    s = [int(k) for k in s]
    c = Counter(s)
    flag = False
    for k in [1,4,6,8,9]:
        if k in c and c[k] >= 1:
            print(1)
            print(k)
            flag = True
            break
    if flag:
        continue
    for k in [2,3,5,7]:
        if k in c and c[k] >= 2:
            print(2)
            print(k*10 + k)
            flag = True
            break
    if flag:
        continue
    comps = {25: 25, 27: 27, 72: 72, 52: 52, 32:32, 35:35, 57:57, 75:75, 
    237:27, 235:25, 372:32, 375:35,732:32,735:35,532:32,537: 57}
    print(2)
    num = 0
    digits = 0
    for k in s:
        num *= 10
        num += k
        digits += 1
        if num in comps:
            print(comps[num])
            break



