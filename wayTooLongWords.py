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
def invr():
    # integer generator 
    return map(int,input().split())

# 71 A

tests = inp()
for _ in range(tests):
    string = input_string()
    if len(string) > 10:
        print(string[0] + str(len(string) - 2) + string[-1])
    else:
        print("".join(string))

