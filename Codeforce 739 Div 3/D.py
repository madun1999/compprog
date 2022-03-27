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

# Codeforce 739 Div 3 D

a = [[int(d) for d in str(2 ** n)] for n in range(80)]

def edit_distance(n,p):
    n = [int(d) for d in str(n)]
    idx = 0
    edit = 0
    for i, d in enumerate(n):
        if d == p[idx]:
            idx += 1
        else:
            edit += 1
        if idx == len(p):
            break
    edit += len(n) - i - 1
    edit += len(p) - idx
    return edit

tests = inp()
for _ in range(tests):
    n = inp()
    mini = 30
    for p in a:
        mini = min(mini, edit_distance(n, p))
        if mini == 0:
            break
    print(mini)