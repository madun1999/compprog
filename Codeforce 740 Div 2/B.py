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


# Codeforce 740 Div 2 B
tests = inp()
for _ in range(tests):
    a,b  = input_int_gen()
    if a > b:
        a, b = b, a
    n = a + b
    s = n // 2
    t = n - s
    # 1 a-s b-t
    forced1 = b - s
    most1 = a + t

    # 2 a-t b-s
    if n % 2:
        forced2 = b - t
        most2 = a + s
        ret = list(range(n - most1, n-forced1 + 1, 2)) + list(range(n - most2, n-forced2 + 1, 2))
        print(len(ret))
        print(" ".join(str(x) for x in sorted(ret)))
    else:
        ret = list(range(n - most1, n-forced1 + 1, 2))
        print(len(ret))
        print(" ".join(str(x) for x in ret))
