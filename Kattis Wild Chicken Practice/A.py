from collections import Counter
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


def make_number(length, msb, lsb):
    return msb * 10 ** (length-1) + (10 ** (length - 1) - 1) // 9 * lsb

# ICPC NAQ 2021 A

tests = 1
for _ in range(tests):
    a = input_string()
    a = [int(x) for x in a]
    a_int = 0
    counter = Counter(a)
    valids = set()
    for i in range(10):
        if counter[i] == 0:
            valids.add(i)
    if not valids:
        print("Impossible")
        continue
    for i in a:
        a_int *= 10
        a_int += i
    lowest = min(valids)
    highest = max(valids)
    lowest_nonzero = min((x for x in valids if x != 0), default=0)
    if lowest_nonzero == 0:
        print(0)
        continue
    candit = []

    higher_msb = [i for i in valids if i > a[0]]
    if higher_msb:
        high_msb = min(higher_msb)
        candit.append(make_number(len(a), high_msb, lowest))
    else:
        candit.append(make_number(len(a)+1, lowest_nonzero, lowest))
    
    lower_msb = [i for i in valids if i < a[0]]
    if lower_msb:
        low_msb = max(lower_msb)
        candit.append(make_number(len(a), low_msb, highest))
    else:
        candit.append(make_number(len(a)-1, highest, highest))
    
    rets = []
    diff = float('inf')
    for i in candit:
        if abs(i - a_int) < diff:
            rets = [i]
            diff = abs(i - a_int)
        elif abs(i- a_int) == diff:
            rets.append(i)
    print(" ".join(str(x) for x in sorted(rets)))
