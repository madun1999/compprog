from collections import defaultdict
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
    # return list(s[:len(s) - 1])
    return s[:-1]
def input_string_l():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())
def print_list(a):
    print(" ".join(str(x) for x in a))

# MAXDISTKT
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    a_sorted = sorted(a)
    dic = defaultdict(list)
    i = 0
    for x in a_sorted:
        if i < x:
            dic[x].append(i)
            i += 1
        else:
            dic[x].append(0)
    ret = []
    for x in a:
        ret.append(dic[x].pop())
    print_list(ret)

