from collections import defaultdict
from math import gcd
import sys
import heapq
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
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]


# ICPC NAQ 2021 C
# from collections import Counter
from itertools import combinations
from operator import mul
from functools import reduce
def get_res(n):
    prime = primes[:n]
    l = n % 2
    sum = 0
    for i in range(n):
        for k in combinations(prime, i):
            if i % 2 == l:
                sum -= reduce(mul, k, 1)
                # print(k , "-")
            else:
                sum += reduce(mul, k, 1)
                # print(k, "+")
    return sum

tests = 1
for _ in range(tests):
    n = inp()
    p = 1
    idx = 0
    while p <= n:
        p *= primes[idx]
        idx += 1
        # print(p)
    idx -= 1
    p = p // primes[idx]

    num = get_res(idx)
    dem = p
    g = gcd(num, dem)
    print(str(num // g) + "/" + str(dem // g))

     