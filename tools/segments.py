from collections import defaultdict
from sortedcontainers import SortedList
from heapq import heappush, heappop, heappushpop
class Segments:
    def __init__(self, k) -> None:
        self.points = SortedList()
        self.points.add(0)
        self.values = defaultdict(list)
        self.singleton_values = defaultdict(list)
        self.k = k

    def add_segment(self, l, r, value):
        if l == r:
            if l not in self.points:
                self.points.add(l)
                li = self.points.index(l)
                vli1 = self.points[li-1]
                self.update(self.values[l], self.values[vli1])
            self.update(self.singleton_values[l], value)
        else:
            r += 1
            lc = True
            rc = True
            if l not in self.points:
                self.points.add(l)
                lc = False
            if r not in self.points:
                self.points.add(r)
                rc = False
            li = self.points.index(l)
            vli1 = self.points[li-1]
            ri = self.points.index(r)
            vri1 = self.points[ri-1]
            if not lc:
                self.values[l] = self.values[vli1]
            if not rc:
                self.values[r] = self.values[vri1]
            for i in range(li, ri):
                vi = self.points[i]
                self.update(self.values[vi], value)

    def update(self, value : list, new_value):
        if len(value) >= self.k:
            heappushpop(value, new_value)
        else:
            heappush(value)
    
    def query(self):
        maxi = 0
        for point, v in self.values.items():
            v += self.singleton_values[point]
            maxi = max(maxi, sum(sorted(v)[:self.k]))
        return maxi