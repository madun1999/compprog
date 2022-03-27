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


# Codeforce 740 Div 2 C
from math import sqrt
tests = inp()
for _ in range(tests):
    n = inp() # number of caves
    caves = []
    cave_nums = []
    for _ in range(n):
        a = input_list()
        cave_nums.append(a[0]) # number of monsters in each cave
        caves.append(a[1:]) # armor of each monster

    cave_stat = []
    for m, a in zip(cave_nums, caves):
        a_t = [x - i for i, x in enumerate(a)]
        cave_stat.append((m, max(a_t) + 1))
    
    cave_stat.sort(key = lambda a: a[1])
    # print(caves)
    # print(cave_stat)
    power = 0
    added = 0
    for add, enter in cave_stat:
        if power + added < enter:
            power = enter - added
        added += add
    
    print(power)

