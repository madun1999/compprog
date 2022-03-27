from collections import defaultdict, deque
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

def cost(colors, costs, line):
    total = 0
    color_list = {}
    for i, v in enumerate(line):
        total += costs[colors[i % 3]][v-1]
        color_list[v] = colors[i % 3] + 1
    return total, color_list

# Codeforce UCSD fa22 W1 C
# from collections import Counter
import heapq
tests = 1
for _ in range(tests):
    n = inp()
    ps = []
    for _ in range(n):
        x, w = input_int_gen()
        ps.append((x-w, x+w))

    ps.sort()
    max_clique = 1
    # print(ps)
    
    # tail_h = []
    # for a, b in ps:
    #     while tail_h and tail_h[0] < a:
    #         heapq.heappop(tail_h)
    #     heapq.heappush(tail_h, b)
    #     if len(tail_h) > max_clique:
    #         max_clique = len(tail_h)
    #     # print(tail_h)
    # print(max_clique)


    last = ps[0][1]
    for a, b in ps[1:]:
        if a >= last:
            max_clique += 1
            last = b
        else:
            if b < last:
                last = b
        # print(a,b,last)
    print(max_clique)