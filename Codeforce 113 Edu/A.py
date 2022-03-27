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


# Codeforce 742 Div 2 A
tests = inp()
for _ in range(tests):
    n = inp()
    s = input_string()
    if s[0] == "a":
        if "b" not in s:
            print(-1, -1)
        else:
            i = s.index("b")
            print(i, i+1)
    else:
        if "a" not in s:
            print(-1, -1)
        else:
            i = s.index("a")
            print(i, i+1)
    

    
