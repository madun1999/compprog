
from collections import defaultdict
import sys
input = sys.stdin.buffer.readline
 
############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_gen_list():
    return input()[:-1].split()
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
 
# Kattis 2021 NA Regionals Practice 4 E

# Modified AccelAsc
# Generating All Partitions: A Comaprison of Two Encodings
# Secion 4.1.2
# Kelleher, Jerome; O'Sullivan, Barry
# prerequisite: length >= 1, sumi >= 0
def partitions(sumi, length, arr, start):
    for i in range(length): # clear array
        arr[i+start] = 0
    if sumi == 0:
        yield None
        return
    if length == 1:
        arr[0] = sumi
        yield None
        return
    k = 1 # index
    y = sumi - 1 # remaining sum
    while k != 0:
        k -= 1
        x = arr[k + start] + 1 
        while 2 * x <= y and k <= length - 3:
            arr[k + start] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            arr[k + start] = x
            arr[l + start] = y
            yield None
            x += 1
            y -= 1
        y += x - 1
        arr[k + start] = y + 1
        arr[l + start] = 0
        yield None

    
# end of partition

mem = [[[[[[[[[[0 for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)] for _ in range(6)]
def get(l):
    return mem[l[0]][l[1]][l[2]][l[3]][l[4]][l[5]][l[6]][l[7]][l[8]][l[9]]

tests = 1
for _ in range(tests):
    n,m,d = input_int_gen()
    mine = input_list()
    opponent = input_list()
    k = mine + opponent
    mine_total = sum(mine)
    opponent_total = sum(opponent)
    total = mine_total + opponent_total
    mine_len = len(mine)
    opponent_len = len(opponent)
    old_dics = defaultdict(int)
    old_dics[(tuple(mine),tuple(opponent))]= 1
    win = 0
    # print(old_dics)
    while d > 0:
        d -= 1
        total -= 1

        new_dics = defaultdict(int)
        new_dics["win"] = old_dics["win"]
        for inner_mine_total in range(max(0, total - opponent_total), mine_total+1):
            inner_opp_total = total - inner_mine_total
            inner_mine = [0 for _ in range(mine_len)]
            inner_opp = [0 for _ in range(opponent_len)]
            # print(inner_mine_total, inner_opp_total)
            for _ in partitions(inner_mine_total, mine_len, inner_mine, 0):
                # print(inner_mine)
                for _ in partitions(inner_opp_total, opponent_len, inner_opp, 0):
                    inner_mine_f = list(filter(lambda x : x != 0, inner_mine))
                    inner_opp_f = list(filter(lambda x: x != 0, inner_opp))
                    dic_key = (tuple(inner_mine_f), tuple(inner_opp_f))
                    # print(dic_key)
                    ll = len(inner_mine_f) + len(inner_opp_f)
                    if not inner_opp_f:
                        dic_key = "win"
                    else:
                        # mine + 1
                        
                        for idx in range(len(inner_mine_f)):
                            inner_mine_f[idx] += 1
                            
                            new_dics[dic_key] += old_dics[(tuple(sorted(inner_mine_f)), tuple(inner_opp_f))] / ll * inner_mine_f.count(inner_mine_f[idx]) / (inner_mine_f.count(inner_mine_f[idx]-1) + 1)
                            inner_mine_f[idx] -= 1
                        new_dics[dic_key] +=  old_dics[(tuple([1] + inner_mine_f), tuple(inner_opp_f))] / (ll + 1) * (inner_mine_f.count(1)+1)
                    # opponent + 1
                    # print(dic_key)
                    for idx in range(len(inner_opp_f)):
                        inner_opp_f[idx] += 1
                        # print(inner_opp_f)
                        # print(old_dics[(tuple(inner_mine_f), tuple(sorted(inner_opp_f)))] / ll * inner_opp_f.count(inner_opp_f[idx]) / (inner_opp_f.count(inner_opp_f[idx]-1) + 1))
                        new_dics[dic_key] += old_dics[(tuple(inner_mine_f), tuple(sorted(inner_opp_f)))] / ll * inner_opp_f.count(inner_opp_f[idx]) / (inner_opp_f.count(inner_opp_f[idx]-1) + 1)
                        inner_opp_f[idx] -= 1
                    new_dics[dic_key] += old_dics[(tuple(inner_mine_f), tuple([1] + inner_opp_f))] / (ll + 1) * (inner_opp_f.count(1)+1)
        att = []
        for keyyy, valueee in new_dics.items():
            if valueee == 0.0:
                att.append(keyyy)
        for keyyy in att:
            del new_dics[keyyy]
        # print(new_dics)
        old_dics = new_dics
    print(old_dics["win"])


        
    