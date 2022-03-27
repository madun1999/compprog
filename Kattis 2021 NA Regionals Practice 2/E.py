
import sys
input = sys.stdin.buffer.readline
 
############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input()[:-1].split()
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
 
# Kattis 2021 NA Regionals Practice 2 E
from collections import defaultdict
tests = 1
for _ in range(tests):
    d, t, c, r = input_gen_list()
    rain_ps = [0 for _ in range(d+1)]
    rain_info = []
    for _ in range(c):
        s, e, p, a = input_gen_list()
        rain_info.append((s, p * a))
        rain_info.append((e, -p * a))
    rain_info.sorted()

    time = 0
    for ti, e in range():
        
    