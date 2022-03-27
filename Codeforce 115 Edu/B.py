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


# Codeforce 115 Edu B
tests = inp()
for _ in range(tests):
    n = inp()
    k = {0:0, 1:0, 2:0, 3:0, 4:0}
    l = []
    for _ in range(n):
        a = input_list()
        l.append(a)
    flag = False
    for i in range(4):
        for j in range(i+1, 5):
            ii, jj, ij = 0, 0, 0
            for a in l:
                if a[i] and a[j]: ij +=1
                elif a[i]: ii += 1
                elif a[j]: jj += 1
            if ii + jj + ij == n and ii + ij >= n // 2 and jj + ij >= n // 2:
                print("YES")
                flag = True
                break
        if flag: break
    if not flag:
        print("NO")
