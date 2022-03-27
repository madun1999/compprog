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
    
def output(s, test):
    print(f"Case #{test+1}: {s}")

def input_digit_list():
    return [int(x) for x in input_string()]
# Codeforce 743 Div 2 A
tests = inp()
for test in range(tests):
    n = inp()
    s = input_digit_list()
    ret = 0
    cons = 0
    first = True
    for c in s:
        if c == 0:
            cons += 1
        else:
            if first:
                ret += (1 + cons) * cons // 2
            else:
                half = cons // 2
                ret += (1 + half) * half
                if cons % 2 == 1:
                    ret += cons // 2 + 1
            first = False
            cons = 0
    ret += (1 + cons) * cons // 2
    output(ret, test)
    
