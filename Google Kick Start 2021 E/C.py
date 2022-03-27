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


from collections import defaultdict

data = defaultdict(lambda : -1)
#### disjoint sets #### https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d
def find(data, i):
    if data[i] != -1:
        data[i] = find(data, data[i])
        return data[i]
    return i
def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj
def connected(data, i, j):
    return find(data, i) == find(data, j)

# Google Kick Start 2021 Round E 
# Question 3 Palindromic Crossword
from collections import Counter, defaultdict
tests = inp()
for test in range(tests):
    N, M = input_int_gen()
    board = []
    for i in range(N):
        board.append(input_string())
    def find_palindromes(i,j):
        global board
        for i = 
    for i in range(N):
        for j in range(M):
            find_palindromes(i,j)
    

    print(f"Case #{test+1}:", ret)