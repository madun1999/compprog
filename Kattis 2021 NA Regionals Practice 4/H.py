import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_list():
    # list of integers
    return list(map(int,input().split()))
def input_string_list():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_string():
    # list of characters
    s = input()
    return s[:len(s) - 1]
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# Kattis 2021 NA Regionals Practice 4 H
tests = 1
for _ in range(tests):
    l,m = input_int_gen()
    mini, min_l = float("inf"), []
    for _ in range(m):
        s = input_string()
        ss = s.split(",")
        # print(s, ss)
        name = ss[0]
        p = int(ss[1])
        c = int(ss[2])
        t = int(ss[3])
        r = int(ss[4])
        # print(name, c*t*10080, (r+t)*l)
        if c * t * 10080 >= (r+t) * l:
            # print(name)
            if p == mini:
                min_l.append(name)
            elif p < mini:
                mini = p
                min_l = [name]
    for name in min_l:
        print(name)
    if not min_l:
        print("no such mower")
