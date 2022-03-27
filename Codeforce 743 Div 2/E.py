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

def par_value(a, b): 
    if a is None:
        return b
    if b is None:
        return a
    l1, ls1, t1, rs1, r1, s1 = a
    l2, ls2, t2, rs2, r2, s2 = b
    lr_sorted = r1 <= l2
    l = l1
    ls = ls1 if not s1 else ((ls1 + ls2) if lr_sorted else ls1)
    rs = rs2 if not s2 else ((rs2 + rs1) if lr_sorted else rs2)
    r = r2
    t = t1 + t2
    if lr_sorted:
        if not s1 and not s2:
            t += lss(rs1 + ls2)
        else:
            t += 0
    else:
        if not s1:
            t += lss(rs1)
        if not s2:
            t += lss(ls2)

    s = s1 and s2 and lr_sorted

    return (l, ls, t, rs, r, s)

# segment tree from https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
# limit for array size
n = 262144
# n = 8
# Max size of tree
tree = [None] * (2 * n) # left, left_size, unsorted_total, right_size, right, sorted
# function to build the tree
def build(arr):
    # insert leaf nodes in tree
    for i in range(len(arr)):
        tree[n + i] = (arr[i], 1, 0, 1, arr[i], True)
    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = par_value(tree[i << 1], tree[i << 1 | 1])
# function to update a tree node
def updateTreeNode(p, value):
    # set value at position p
    tree[p + n] = (value, 1, 0, 1, value, True)
    p = p + n
    # move upward and update parents
    i = p
    while i > 1 :
        il = (i >> 1) << 1
        tree[i >> 1] = par_value(tree[il], tree[il ^ 1])
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


# Codeforce 743 Div 2 E
tests = inp()
for _ in range(tests):
    pass


