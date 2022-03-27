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
def invr():
    # integer generator 
    return map(int,input().split())


# Codeforce 736 Div 2 B

tests = inp()
for _ in range(tests):
    size = inp()
    enemy = input_string()
    geo = input_string()
    # print(enemy, geo)
    passed = 0
    for i in range(size):
        e = enemy[i]
        g = geo[i]
        if e == "0" and g == "1":
            passed += 1
        elif e == "1" and g == "1":
            if i >= 1 and enemy[i-1] == "1":
                enemy[i-1] = "0"
                passed += 1
            elif i < size - 1 and enemy[i+1] == "1":
                enemy[i+1] = "0"
                passed += 1
    print(passed)
