from collections import defaultdict
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input().split()
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

MOD = 10 ** 9 + 7

def neg(prob):
    return (- prob) % MOD

# Google Kick Start 2021 H Problem B
tests = inp()
ONE_PROB = 10 ** 6
for test in range(tests):
    n, q = input_int_gen()
    one_probes = 0
    cond_probs_parent = [(0,0) for _ in range(n + 1)] # occurs, not occur
    cond_probs_parent[1] = None
    cond_probs_one = [None for _ in range(n + 1)] # occurs, not occur
    cond_probs_one[1] = (1, 0) # occurs, not occur
    parents = [0 for _ in range(n + 1)]
    parents[1] = 1
    one_probes = inp()
    for i in range(2, n+1):
        p, a, b = input_int_gen()
        parents[i] = p
        cond_probs_parent[i] = (a, b)
    
    def given(t):
        # return prob * 10 ^ 6 of (event t given event 1, t given not 1)
        cur = t
        stk = []
        # find first ancestor with cond. prob
        while cond_probs_one[cur] is None:
            stk.append(cur)
            cur = parents[cur]
        
        # cur is first ancestor with cond. prob
        while stk:
            child = stk.pop()
            # compute & store P(child|1) and P(child|not 1)
            child_given_cur = cond_probs_parent[child][0]
            child_given_ncur = cond_probs_parent[child][1]
            cur_given_one = cond_probs_one[cur][0]
            ncur_given_one = neg(cur_given_one)
            cur_given_notone = cond_probs_one[cur][1]
            ncur_given_notone = neg(cur_given_notone)

            child_given_one = (child_given_cur * cur_given_one  + child_given_ncur * ncur_given_one) % MOD
            child_given_notone = (child_given_cur * cur_given_notone + child_given_ncur * ncur_given_notone) % MOD
            cond_probs_one[child] = (child_given_one, child_given_notone)

            cur = child

        # cur is t
        return cond_probs_one[cur]

    ret = []
    for _ in range(q):
        u, v = input_int_gen()
        v_one, v_notone = given(v)
        u_one, u_notone = given(u)
        
        total = (v_one * u_one * one_probes + v_notone * u_notone * neg(one_probes)) % MOD
        ret.append(total)

    print(f"Case #{test+1}:", " ".join([str(x) for x in ret]))