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

# ICPC NAQ 2021 M
tests = inp()
for _ in range(tests):
    a = input()
    n = int(a, 8)
    l = list(reversed([int(i) for i in bin(n)[2:]]))
    l = l + ([0] * (18 - len(l)))
    # print(l)
    board = [[-1 for _ in range(3)] for _ in range(3)]
    for idx in range(9):
        board[idx // 3][idx % 3] = -1 if l[idx] == 0 else l[idx+9]

    winner = -1 
    # 0: O wins
    # 1: X wins
    # 2: Cat's
    # 3: In progress
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != -1:
            winner = board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != -1:
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != -1:
            winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != -1:
            winner = board[0][2] 
    
    if winner == -1:
        if any([board[x // 3][x % 3]==-1 for x in range(9)]):
            winner = 3
        else:
            winner = 2
    if winner == 0:
        print("O wins")
    elif winner == 1:
        print("X wins")
    elif winner == 2:
        print("Cat's")
    elif winner == 3:
        print("In progress")

    
    

