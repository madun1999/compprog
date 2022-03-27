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

def output(s, test):
    print(f"Case #{test+1}: {s}")

from collections import defaultdict
from bisect import bisect_left
from heapq import heappush, heappushpop
class Segments:
    def __init__(self, k) -> None:
        self.points = [0]
        self.values = defaultdict(list)
        self.singleton_values = defaultdict(list)
        self.k = k

    def add_segment(self, l, r, value):
        if l == r:
            if l not in self.points:
                iii = bisect_left(self.points, l)
                self.points.insert(iii, l)
                li = self.points.index(l)
                vli1 = self.points[li-1]
                self.values[l] = self.values[vli1].copy()
            self.update(self.singleton_values[l], value)
        else:
            r += 1
            lc = True
            rc = True
            if l not in self.points:
                iii = bisect_left(self.points, l)
                self.points.insert(iii, l)
                lc = False
            if r not in self.points:
                iii = bisect_left(self.points, r)
                self.points.insert(iii, r)
                rc = False
            li = self.points.index(l)
            vli1 = self.points[li-1]
            ri = self.points.index(r)
            vri1 = self.points[ri-1]
            if not lc:
                self.values[l] = self.values[vli1].copy()
            if not rc:
                self.values[r] = self.values[vri1].copy()
            # print(self.points, li, ri)
            # print(self.values)
            for i in range(li, ri):
                vi = self.points[i]
                self.update(self.values[vi], value)
            # print(self.values)

    def update(self, value : list, new_value):
        if len(value) >= self.k:
            heappushpop(value, new_value)
        else:
            heappush(value, new_value)

    def query(self):
        maxi = 0
        for point, v in self.values.items():
            # print(v)
            v += self.singleton_values[point]
            # print(v)
            maxi = max(maxi, sum(sorted(v)[:self.k]))
        return maxi

# Google Kick Start 2021 Round F B
tests = inp()
for test in range(tests):
    d, n, k = input_int_gen()
    segs = Segments(k)
    for i in range(1, n+1):
        v, l, r = input_int_gen()
        segs.add_segment(l, r, v)
    
    output(str(segs.query()) , test)