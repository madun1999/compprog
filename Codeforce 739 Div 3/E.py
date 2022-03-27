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

def list_to_string(s):
    return ''.join(s)

# Codeforce 739 Div 3 E
from collections import Counter
tests = inp()
for _ in range(tests):
    t = input_string()
    count = len(set(t))
    removed = []
    removed_set = set()
    t_counter = Counter(t)
    for c in reversed(t):
        if c not in removed_set:
            removed.append(c)
            removed_set.add(c)
    removed.reverse()    
    s_length = 0
    note = False
    s_count = Counter()
    for idx, c in enumerate(removed):
        if t_counter[c] % (idx + 1) != 0:
            print(-1)
            note = True
            break
        s_length += t_counter[c] // (idx + 1)
        s_count[c] = t_counter[c] // (idx + 1)
    if note:
        continue
    s = t[:s_length]
    if Counter(s) != s_count:
        print(-1)
        continue

    
    idx = len(s)
    for c in removed:
        s = [x for x in s if x != c]
        if t[idx:idx + len(s)] != s:
            note = True
            break
        idx += len(s)
    if note:
        print(-1)
    else:
        print(list_to_string(t[:s_length]),list_to_string(removed))