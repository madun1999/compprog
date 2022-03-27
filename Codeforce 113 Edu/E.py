from math import atan2
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

def lss(n):
    return (n * (n + 1)) // 2

def par_value(a, b, c): 
    a1, a2 = a
    b1, b2 = b
    return (a1, c) if c else (b1, c)
# segment tree from https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
# limit for array size
n = 32
# n = 8
# Max size of tree
tree = [None] * (2 * n) # left, left_size, unsorted_total, right_size, right, sorted
# function to build the tree
def build(arr):
    # insert leaf nodes in tree
    for i in range(len(arr)):
        tree[n + i] = (i, 0)
    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = par_value(tree[i << 1], tree[i << 1 | 1], 0)
# function to update a tree node
def updateTreeNode(p, value):
    # set value at position p
    # p = p + n
    tree[p] = par_value(tree[p << 1], tree[p << 1 | 1], ~tree[p][1])
    # move upward and update parents
    i = p
    while i > 1 :
        il = (i >> 1) << 1
        tree[i >> 1] = par_value(tree[il], tree[il ^ 1], tree[i >> 1][1])
        i >>= 1
 
# function to get sum on interval [l, r)
def query(l, r) :
    res_left = None
    res_right = None
    # loop to find the sum in the range
    l += n
    r += n
    while l < r :
        if (l & 1) :
            if res_left is None:
                res_left = tree[l]
            else:
                res_left = par_value(res_left, tree[l])
            l += 1
        if (r & 1) :
            r -= 1
            if res_right is None:
                res_right = tree[r]
            else:
                res_right = par_value(tree[r],res_right)
        l >>= 1
        r >>= 1
    res_node = par_value(res_left, res_right)
    # print(res_node)
    res = res_node[2] + lss(res_node[1]) + (lss(res_node[3]) if not res_node[5] else 0)
    return res


# Codeforce 742 Div 2 D
MOD = 998_244_353
# tests = inp()
tests = 1
for _ in range(tests):
    k, A, h = input_int_gen()
    m = 2 ** k 
    remains = list(range(1, n+1))
    for i in range(2 ** (n - 1)):
        for j in range(n-1):
            if i % 2:
                pass
            else:
                pass
            i = i >> 1



