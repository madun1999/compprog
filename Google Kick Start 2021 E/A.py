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


# Google Kick Start 2021 Round E 
# Question 1 Shuffled Anagrams
from collections import Counter, defaultdict
tests = inp()
for test in range(tests):
    s = input_string()
    n = len(s)
    n1 = n
    ret = [None for c in s]
    counter = Counter(s)
    mc, mcount = counter.most_common(1)[0]
    if mcount * 2 > n:
        print(f"Case #{test+1}: IMPOSSIBLE")
        continue

    idxes = defaultdict(list)
    for idx, c in enumerate(s):
        idxes[c].append(idx)

    swaps = dict()
    def rotate(a, b, c):
        global n1, counter, idxes
        idxa = idxes[a].pop()
        idxb = idxes[b].pop()
        idxc = idxes[c].pop()
        ret[idxa] = b
        ret[idxb] = c
        ret[idxc] = a
        n1 -= 3
        counter = +(counter - Counter([a,b,c]))

    def swap(a, b):
        global n1, counter, idxes
        idxa = idxes[a].pop()
        idxb = idxes[b].pop()
        # print(idxa, idxb)
        ret[idxa] = b
        ret[idxb] = a
        n1 -= 2
        counter = +(counter - Counter([a,b]))

    while n1 > 3:
        most_commons_two = counter.most_common(2)
        mc = most_commons_two[0][0]
        mc2 = most_commons_two[1][0]
        # print(mc, mc2, counter)
        swap(mc, mc2)
    if n1 == 3:
        mct = counter.most_common(3)
        a = mct[0][0]
        b = mct[1][0]
        c = mct[2][0]
        rotate(a,b,c)
    if n1 == 2:
        mct = counter.most_common(2)
        a = mct[0][0]
        b = mct[1][0]
        swap(a,b)
    print(f"Case #{test+1}:", ''.join(ret))