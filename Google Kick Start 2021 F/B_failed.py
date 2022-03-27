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

h = {0:0}

# segment tree edited from https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
# edited by madun1999
class segmentTree:
    def __init__(self, length, k):
        self.k = k
        self.length = length
        if length == 1:
            self.seg_tree_cap = 2
        self.seg_tree_cap = 1<<length.bit_length()
        self.tree = [self.default_leaf()] * (2 * self.seg_tree_cap + 1)
        self.value = [self.default_leaf()] * (2 * self.seg_tree_cap + 1)
 

    # function to query on interval [l, r)
    def query(self, l, r):
        res_left = self.default_leaf()
        res_right = self.default_leaf()
        # loop to find the sum in the range
        l += self.seg_tree_cap
        r += self.seg_tree_cap
        while l < r :
            if (l & 1) :
                if res_left is None:
                    res_left = self.tree[l]
                else:
                    res_left = self.child_to_parent(res_left, self.tree[l], self.value[l])
                l += 1
            if (r & 1) :
                r -= 1
                if res_right is None:
                    res_right = self.tree[r]
                else:
                    res_right = self.child_to_parent(self.tree[r], res_right, self.value[r])
            l >>= 1
            r >>= 1
        res_node = self.child_to_parent(res_left, res_right)
        return res_node
    
    def updateRangeValue(self, l, r, value):
        res_left = None
        res_right = None
        # loop to find the sum in the range
        l += self.seg_tree_cap
        r += self.seg_tree_cap
        if l == r:
            self.updateTreeNode(l - self.seg_tree_cap, value)
        while l < r :
            if (l & 1) :
                if l > self.seg_tree_cap:
                    self.updateTreeNode(l - self.seg_tree_cap, value)
                else:
                    self.value[l] = value
                l += 1
            if (r & 1) :
                r -= 1
                if r > self.seg_tree_cap:
                    self.updateTreeNode(r - self.seg_tree_cap, value)
                else:
                    self.value[r] = value
            l >>= 1
            r >>= 1

    def updateTreeNode(self, p, value):
        # set value at position p
        self.tree[p + self.seg_tree_cap] = self.update_leaf(self.tree[p + self.seg_tree_cap], value)
        p = p + self.seg_tree_cap
        # move upward and update parents
        i = p
        while i > 1 :
            self.tree[i >> 1] = self.parent_from_stored_child(i >> 1)
            i >>= 1

    def build_with_arr(self, arr):
        assert len(arr) == self.length
        # insert leaf nodes in tree
        for i in range(self.length):
            self.tree[self.seg_tree_cap + i] = self.leaf_from_array(arr[i])
        # build the tree by calculating parents
        for i in range(self.seg_tree_cap - 1, 0, -1):
            self.tree[i] = self.parent_from_stored_child(i)

    def build_default(self):
        # insert leaf nodes in tree
        for i in range(self.length):
            self.tree[self.seg_tree_cap + i] = self.default_leaf()
        # build the tree by calculating parents
        for i in range(self.seg_tree_cap - 1, 0, -1):
            self.tree[i] = self.parent_from_stored_child(i)


    def default_leaf(self):
        #### edit this
        return []
        
    def leaf_from_array(self, value):
        #### edit this
        return [value]

    def child_to_parent(self, left, right, value=None):
        #### edit this 
        return sorted(set(left + right + (value if value else [])), reverse=True, 
                key=lambda x: h[x])[:self.k]
    
    def parent_from_stored_child(self, par):
        # print(par, self.seg_tree_cap)
        left, right, value = self.tree[par << 1], self.tree[par << 1 | 1], self.value[par]
        return self.child_to_parent(left, right, value)
    
    def update_leaf(self, old_value, value):
        return sorted(set(old_value + value), reverse=True, key=lambda x: h[x])[:self.k] 
        
# Codeforce 743 Div 2 B
tests = inp()
for test in range(tests):
    d, n, k = input_int_gen()
    tree = segmentTree(d, k)
    tree.build_default()
    # print(tree.tree)
    # print(tree.value)
    # print()
    h = {0:0}
    for i in range(1, n+1):
        v, l, r = input_int_gen()
        h[i] = v
        tree.updateRangeValue(l, r, [i])
        # print(tree.tree)
        # print(tree.value)
        # print()
    # print(h)
    ans = tree.tree[1]
    # print(ans)
    output(str(sum([h[x] for x in ans])) , test)