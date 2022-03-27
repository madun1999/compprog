from collections import defaultdict
import sys
input = sys.stdin.buffer.readline

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

def descendents(children, root):
    # return set of descendents including root
    stk = [root]
    res = {}
    while stk:
        cur = stk.pop()
        res.add(cur)
        stk.extend(children[root])
    return res

def query(a):
    print(f"? {n} {' '.join(a)}")
    sys.stdout.flush()
    ret = inp()
    return ret

# Codeforce 746 Div 2 D
tests = inp()
for _ in range(tests):
    n = inp()
    edges = defaultdict(set)
    for _ in range(n-1):
        u, v = input_int_gen()
        edges[u].add(v)
        edges[v].add(u)
    
    target = query(range(1, n+1))

    stk = [(1, False, -1)]
    counts = [0 for _ in range(n+1)]
    parents = [0 for _ in range(n+1)]
    children = [set() for _ in range(n+1)]
    while stk:
        node, visited, par = stk.pop()
        # print(node, visited, par)
        if visited:
            children[node] = set(t for t in edges[node] if t != par)
            counts[node] = 1 + sum(counts[t] for t in children[node])
            parents[node] = par
        else:
            stk.append((node, True, par))
            for x in edges[node]:
                if x != par:
                    stk.append((x, False, node))
    
    rem_edges = set(range(2, n + 1))
    roots = {1}
    while len(rem_edges) != 1:
        # one query per iter
        half_edges = len(rem_edges) // 2
        cur_edges = {}
        while len(cur_edges) != half_edges:
            root = roots.pop()
            if counts[root] < half_edges:
                temp = descendents(children, root) - {root}
                cur_edges.update(temp)
                rem_edges -= temp
                half_edges -= len(temp)
            else:
                if len(children[root]) < half_edges:
                    cur_edges.update(children[root])
                    half_edges -= len(children[root])
                    roots.update(children[root])
                    rem_edges -= children[root]
                else:
                    part_child = iter(children[root])[:half_edges]
                    half_edges = 0
                    roots.update(part_child)
                    cur_edges.update(part_child)
                    children[root] -= (part_child)
                    rem_edges -= part_child
            # do query
            ans = query(cur_edges)
            # update result







