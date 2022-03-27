from collections import defaultdict
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

# Codeforce UCSD fa22 W6 E
tests = 1
for _ in range(tests):
    N = inp()
    xs = defaultdict(set)
    ys = defaultdict(set)
    for _ in range(N):
        x, y = input_int_gen()
        xs[x].add(y)
        ys[y].add(x)
    count = 0
    for x, yy in xs.items():
        yyl = sorted(list(yy))
        for i in range(len(yyl)):
            for j in range(i+2, len(yyl)):
                a = yyl[i]
                b = yyl[j]
                if (a + b) % 2 == 0 and (a + b) // 2 in yy:
                    count += len(ys[(a + b) // 2]) - 1
    xs, ys = ys, xs
    for x, yy in xs.items():
        yyl = sorted(list(yy))
        for i in range(len(yyl)):
            for j in range(i+2, len(yyl)):
                a = yyl[i]
                b = yyl[j]
                if (a + b) % 2 == 0 and (a + b) // 2 in yy:
                    count += len(ys[(a + b) // 2]) - 1
    print(count)

