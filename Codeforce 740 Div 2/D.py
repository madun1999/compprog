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

# Codeforce 740 Div 2 D

n, MOD = input_int_gen()
sum = 1
mem = [1]
for i in range(2, n+1):
    now = sum
    k = 0
    for j in range(2, i+1):
        k1 = i // j
        k2 = i // (j + 1)
        if k1 == k2:
            k = k1
            break
        now = (now + mem[k1 - 1]) % MOD
    # print(i, j, k)
    for j in range(1, k+1):
        high = i // j
        low = i // (j+1)
        # print(high, low)
        now = (now + mem[j - 1] * (high - low)) % MOD
    mem.append(now)
    sum = (sum + now) % MOD
print(now)