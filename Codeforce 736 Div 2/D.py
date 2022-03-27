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
def invr():
    # integer generator 
    return map(int,input().split())

# https://stackoverflow.com/questions/25706885/generator-function-for-prime-numbers
def genprimes(limit): # derived from 
                      # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}            # http://code.activestate.com/recipes/117119/
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

# Codeforce 736 Div 2 B
# import heapq
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

tests = inp()
for _ in range(tests):
    size = inp()
    integers = input_list()
    # integers_heap = [x for x in integers]
    # heapq.heapify(integers_heap)

    # M = max(integers)
    # M2 = max(n for n in integers if n != M)
    max_count = 0
    # for m in genprimes(10000):
    for m in primes:
        # while integers_heap[0] < m:
        #     heapq.heappop(integers_heap)
        if max_count >= size:
            break
        count = 0
        num = -1
        for idx in range(size):
            if count + size - idx < max_count:
                break
            i = integers[idx]
            if i % m == num:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                num = i % m
                count = 1
    print(max_count)
