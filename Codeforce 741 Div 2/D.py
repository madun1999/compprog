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

def same_sign(a, b):
    return a * b > 0

def charge_d(l, r, ps):
    return ps[r] - ps[l-1]
def charge_c(l, r, ps):
    return (ps[r] - ps[l-1]) * (1 if l % 2 else -1)

def removed(l,r, s, ps, i):
    charges = charge_c(l, r, ps)
    charges -= s[i-1] * (-1 if (i - l) % 2 else 1)
    if i == r:
        return charges
    charges -= 2 * charge_c(i+1, r, ps) * (1 if (i - l) % 2 else -1)
    return charges

# Codeforce 741 Div 2 D
tests = inp()
charge_dict = {'+': 1, '-': -1}
for _ in range(tests):
    n, q = input_int_gen()
    s = input_string()
    s = [charge_dict[k] for k in s]
    ps = [0]
    for i, k in enumerate(s):
        ps.append(ps[-1] + k * (-1 if i % 2 else 1))
    for i in range(q):
        l,r = input_int_gen()
        rets = []
        charge = charge_c(l, r, ps)
        if charge == 0:
            print(0)
            continue
        if (r-l+1) % 2 == 0:
            rets.append(r)
            r -= 1
            charge = charge_c(l, r, ps)
            print(2)
        else:
            print(1)
        mini = l
        maxi = r
        ret = mini
        temp = []
        while mini < maxi:
            midi = mini + (maxi - mini) // 2
            charge_now = removed(l,r, s, ps, midi)
            if charge_now == 0:
                ret = midi
                break
            if same_sign(charge, charge_now):
                maxi = midi
            else:
                mini = midi + 1
            ret = midi
        # print("a", l, r, ret)
        rets.append(ret)
        print(' '.join(str(x) for x in rets))
        
        # print(''.join('+' if x > 0 else '-' for x in s[l:r+1]))
        # print(ret - l+1)
        # print()



