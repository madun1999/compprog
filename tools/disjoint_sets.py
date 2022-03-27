# union find, union by size
# ufd = union_find_data
# initialize data, index 0~n inclusive
def make_ufd(n):
    return ([x for x in range(n+1)], [1 for _ in range(n+1)])

def find(ufd, i):
    data, _ = ufd
    root = i
    while data[root] != root:
        root = data[root]
    while data[i] != root:
        p = data[i]
        data[i] = root
        i = p
    return root

def union(ufd, i, j):
    data, size = ufd
    pi, pj = find(ufd, i), find(ufd, j)
    if pi == pj:
        return
    if size[pi] < size[pj]:
        pi, pj = pj, pi
    data[pj] = pi
    size[pi] += size[pj]


def connected(ufd, i, j):
    return find(ufd, i) == find(ufd, j)

def ufd_size(ufd, i):
    _, size = ufd
    return size[find(ufd, i)]