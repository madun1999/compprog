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
n = 10000 + 1
data = ([-1 for _ in range(n+1)], [0 for _ in range(n+1)])

def find(union_find_data, i):
    data, rank = union_find_data
    if data[i] != -1:
        data[i] = find(union_find_data, data[i])
        rank[i] = 1
        return data[i]
    return i

def union(union_find_data, i, j):
    data, rank = union_find_data
    pi, pj = find(union_find_data, i), find(union_find_data, j)
    if pi != pj:
        if rank[pi] == rank[pj]:
            data[pi] = pj
            rank[pj] += 1
        elif rank[pi] < rank[pj]:
            data[pi] = pj
        else:
            data[pj] = pi


def connected(union_find_data, i, j):
    return find(union_find_data, i) == find(union_find_data, j)

def MST(edge_list, n):
    data = ([-1 for _ in range(n+1)], [0 for _ in range(n+1)])
    weight_sum = 0
    count = 0
    while edge_list:
        w, (a,b) = heapq.heappop(edge_list)
        if not connected(data, a, b):
            weight_sum += w
            union(data, a, b)
            count += 1
            if count == n:
                return weight_sum
    return weight_sum

# Codeforce UCSD fa22 W2 C
# from collections import Counter

tests = inp()
for _ in range(tests):
    n, m, k = input_int_gen()
    # inc_edges = defaultdict(lambda : defaultdict(lambda : -1))
    # dec_edges = defaultdict(lambda : defaultdict(lambda : -1))
    edge_list = []
    
    closest = k
    for _ in range(m):
        a, b, w = input_int_gen()
        closest = min(closest, abs(k-w))
        if k - w >= 0:
            # dec_edges[a][b] = dec_edges[b][a] = 0
            heapq.heappush(edge_list, (0, (a,b)))
            # edge_list.append((0, (a,b)))
            # inc_edges[a][b] = inc_edges[b][a] = k - w
        else:
            heapq.heappush(edge_list, (w-k, (a,b)))
            # edge_list.append((w-k, (a,b)))
            # dec_edges[a][b] = dec_edges[b][a] = w - k
    
    # edge_list.sort()
    mst_weight = MST(edge_list, n)

    if mst_weight > 0:
        print(mst_weight)
    else:
        # print("inc connects")
        print(closest)

        
    

        


