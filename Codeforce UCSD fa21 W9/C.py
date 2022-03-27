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
    # return list(s[:len(s) - 1])
    return s[:-1]
def input_string_l():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# Codeforce UCSD fa21 W9 C
# from collections import Counter
tests = 1
for _ in range(tests):
    n,m = input_int_gen()
    hori = defaultdict(list)
    verti = defaultdict(list)
    slantup = defaultdict(list)
    slantdown = defaultdict(list)
    for _ in range(m):
        a,b = input_int_gen()
        hori[a].append((a,b))
        verti[b].append((a,b))
        slantup[a+b].append((a,b))
        slantdown[a-b].append((a,b))
    
    queenAttacks = defaultdict(int)
    # print(hori)
    # print(verti)
    # print(slantup)
    # print(slantdown)
    for _, queens in hori.items():
        if len(queens) > 1:
            queens.sort(key=lambda r:r[1])
            for i, queen in enumerate(queens):
                if i == 0 or i == len(queens) - 1:
                    queenAttacks[queen] += 1
                else:
                    queenAttacks[queen] += 2
    
    for _, queens in verti.items():
        if len(queens) > 1:
            queens.sort(key=lambda r:r[0])
            for i, queen in enumerate(queens):
                if i == 0 or i == len(queens) - 1:
                    queenAttacks[queen] += 1
                else:
                    queenAttacks[queen] += 2
    
    for _, queens in slantup.items():
        if len(queens) > 1:
            queens.sort(key=lambda r:r[1])
            for i, queen in enumerate(queens):
                if i == 0 or i == len(queens) - 1:
                    queenAttacks[queen] += 1
                else:
                    queenAttacks[queen] += 2
    
    for _, queens in slantdown.items():
        if len(queens) > 1:
            queens.sort(key=lambda r:r[1])
            for i, queen in enumerate(queens):
                if i == 0 or i == len(queens) - 1:
                    queenAttacks[queen] += 1
                else:
                    queenAttacks[queen] += 2
    
    freq = [0 for _ in range(9)]

    total = len(queenAttacks)
    for _, attacks in queenAttacks.items():
        freq[attacks] += 1
    freq[0] = m - total
    
    print(" ".join(str(x) for x in freq))

        

