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


# Codeforce 736 Div 2 B
from collections import defaultdict
# import heapq
noble_size, friendships = input_int_gen()
friends = defaultdict(set)
died = 0
for _ in range(friendships):
    a, b = input_int_gen()
    if b > a:
        if not friends[a]:
            died += 1
        friends[a].add(b)
    else:
        if not friends[b]:
            died += 1
        friends[b].add(a)
query_size = inp()
for _ in range(query_size):
    query = input_list()
    if query[0] == 1:
        a, b = query[1], query[2]
        if b > a:
            if not friends[a]:
                died += 1
            friends[a].add(b)
        else:
            if not friends[b]:
                died += 1
            friends[b].add(a)
    if query[0] == 2:
        a, b = query[1], query[2]
        if b > a:
            friends[a].remove(b)
            if not friends[a]:
                died -= 1
        else:
            friends[b].remove(a)
            if not friends[b]:
                died -= 1
    if query[0] == 3:
        print(noble_size - died)
