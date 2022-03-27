from collections import Counter, defaultdict
import sys

# from matplotlib.pyplot import table
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_float():
    # one float
    return float(input())
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
    return map(int,input().split())

def multi(A, B):
    l = len(A)
    ret = [[0 for _ in range(l)] for _ in range(l)]

    for i in range(l):
        for j in range(l):
            for k in range(l):
                ret[i][j] += B[i][k] * A[k][j]
    return ret

def square(m):
    return multi(m, m)

# Kattis 2021 NA Regionals Practice 2 D
tests = 1
for _ in range(tests):
    r,c,k = input_int_gen()
    n = r * c
    
    target_p = input_float()
    ladders = {}
    for _ in range(k):
        a, b = input_int_gen()
        ladders[a-1] = b-1
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(1,7):
            if i+j < n:
                if i+j in ladders:
                    matrix[i][ladders[i+j]] += 1/6
                else:
                    matrix[i][i+j] += 1/6
            else:
                matrix[i][n-1] += 1/6
    matrices = {1:matrix}
    # print(ladders)
    step = 1
    
    
    # while matrix[0][-1] < int(target_p * (6 ** step)):
    while matrix[0][-1] < target_p:
        matrix = square(matrix)
        step *= 2
        matrices[step] = matrix
    # print(matrices)

    def cut(matrices, target_p, step, mem, t_step): # recursion, max depth 28
        # print(step)
        if step == 1:
            return t_step + 1
        else:
            t = multi(mem, matrices[step // 2])
            # if t[0][-1] > int(target_p * (6 ** step)): 
            if t[0][-1] > target_p:
                return cut(matrices, target_p, step // 2, mem, t_step)
            else:
                return cut(matrices, target_p, step // 2, t, t_step + step // 2)

    ident = [[(1 if i == j else 0) for i in range(n)] for j in range(n)]
    targ = cut(matrices, target_p, step, ident, 0)
    print(targ)

    