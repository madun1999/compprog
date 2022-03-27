# segment tree edited from https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
# edited by madun1999
class segmentTree:
    def __init__(self, length):
        self.length = length
        if length == 1:
            self.seg_tree_cap = 2
        self.seg_tree_cap = 1<<length.bit_length()
        self.tree = [None] * (2 * self.seg_tree_cap)
        self.value = [None] * (2 * self.seg_tree_cap)

    # function to query on interval [l, r)
    def query(self, l, r):
        res_left = None
        res_right = None
        # loop to find the sum in the range
        l += self.seg_tree_cap
        r += self.seg_tree_cap
        while l < r :
            if (l & 1) :
                if res_left is None:
                    res_left = self.tree[l]
                else:
                    res_left = self.child_to_parent(res_left, self.tree[l], self.value)
                l += 1
            if (r & 1) :
                r -= 1
                if res_right is None:
                    res_right = self.tree[r]
                else:
                    res_right = self.child_to_parent(self.tree[r], res_right)
            l >>= 1
            r >>= 1
        res_node = self.child_to_parent(res_left, res_right)
        return res_node

    def updateTreeNode(self, p, value):
        # set value at position p
        self.tree[p + self.seg_tree_cap] = value
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
        return 0
        
    def leaf_from_array(self, value):
        #### edit this
        return value

    def child_to_parent(self, left, right, value=None):
        #### edit this 
        return left + right + value
    
    def parent_from_stored_child(self, par):
        left, right, value = self.tree[par << 1], self.tree[par << 1 | 1], self.value[par]
        return self.child_to_parent(left, right, value)