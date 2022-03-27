from bisect import bisect_left, bisect_right
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

# ICPC NAQ 2021 K
tests = 1
for _ in range(tests):
    m, n = input_int_gen()
    a = input_list()
    sumi = sum(a)
    pre_sum = [0]
    post_sum = [0]
    for i in a:
        pre_sum.append(pre_sum[-1] + i)
    for i in reversed(a):
        post_sum.append(post_sum[-1] + i)

    for _ in range(n):
        target = inp()
        # print(target)
        left = 0
        right = m
        found = False
        while right >= 0 and left + right <= m:
            s = pre_sum[left] + post_sum[right]
            if s == target:
                found = True
                break
            if s > target:
                right -= 1
            if s < target:
                left += 1
        if found:
            print("Yes")
        else:
            print("No")
