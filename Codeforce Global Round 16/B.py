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

# Codeforces Global Round 16 B
tests = inp()
for _ in range(tests):
    n = input_string()
    n = [int(x) for x in n]
    runs_of_zero = 0
    zero = False
    one = False
    for i in n:
        if i == 1:
            one = True
            zero = False
        else:
            if not zero:
                runs_of_zero += 1
            zero = True
    if not one:
        print(1)
    elif runs_of_zero == 0:
        print(0)
    elif runs_of_zero == 1:
        print(1)
    else:
        print(2)
        
        