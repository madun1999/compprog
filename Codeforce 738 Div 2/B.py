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


# Codeforce 738 Div 2 B
dif = {"R":"B", "B":"R"}
tests = inp()
for _ in range(tests):
    size = inp()
    squares = input_string()
    # code here
    if squares[0] == "?":
        idx = 0
        while idx < size and squares[idx] == "?":
            idx += 1
        if idx == size:
            print(("RB" * (size // 2 + 1))[:size])
            continue
        while idx > 0:
            squares[idx-1] = dif[squares[idx]]
            idx -= 1

    for idx in range(size):
        if squares[idx] == "?":
            squares[idx] = dif[squares[idx-1]]
    print(''.join(squares))