from collections import defaultdict
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

# Codeforce UCSD fa22 W6 C


tests = inp()
for _ in range(tests):
    found = False
    a,b,c = input_int_gen()
    for sumi in range(10**4 * 3):
        for i in range(0, sumi+1):
            for j in range(0, sumi - i + 1):
                k = sumi - i - j
                a1 = [a + i, a - i]
                b1 = [b + j, b - j]
                c1 = [c + k, c - k]
                for x in a1:
                    for y in b1:
                        for z in c1:
                            # print(i,j,k,x,y,z)
                            if x > 0 and y > 0 and z > 0 and z % y == 0 and y % x == 0:
                                print(sumi)
                                print(x, y, z)
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    



    

        


