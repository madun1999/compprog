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


# Codeforce 746 Div 2 A
tests = inp()
for _ in range(tests):
    n, H = input_int_gen()
    a = input_list()
    maxi = max(a)
    a.remove(maxi)
    maxi2 = max(a)
    t = H // (maxi + maxi2)
    r = H % (maxi + maxi2)
    if r == 0:
        print(t * 2)
    elif r <= maxi:
        print(t * 2 + 1)
    else:
        print(t * 2 + 2)

    
