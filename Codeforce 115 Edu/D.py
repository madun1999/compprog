from collections import defaultdict
import sys
input = sys.stdin.buffer.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input().split()
def input_list():
    # list of integers
    return list(map(int,input().split()))
def input_string():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().decode().split())


from collections import defaultdict



# Codeforce 115 Edu D
tests = inp()
for _ in range(tests):
    n = inp()
    xs = [0 for _ in range(n + 1)]
    ys = [0 for _ in range(n + 1)]
    points = []
    for _ in range(n):
        a, b = input_int_gen()
        points.append((a,b))
        xs[a] += 1
        ys[b] += 1
    
    res = 0
    for a, b in points:
        res += (xs[a] - 1) * (ys[b] - 1)

    print(n * (n-1) * (n-2) // 6 - res)
