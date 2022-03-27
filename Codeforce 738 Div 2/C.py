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


# Codeforce 738 Div 2 C
tests = inp()
for _ in range(tests):
    n = inp()
    roads = input_list()
    # code here
    ret = []
    for idx, road in enumerate(roads):
        if road == 0:
            ret.append(idx+1)
        if road == 1:
            ret.append(n+1)
            ret.extend(list(range(idx+1, n+1)))
            break
    else:
        ret.append(n+1)
    print(' '.join([str(x) for x in ret]))