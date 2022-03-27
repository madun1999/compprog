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

def largest(using, n_digits):
    return (10 ** n_digits - 1) // 9 * max(using) 
def smallest(using, n_digits, zero_allowed=False):
    if zero_allowed:
        return 0
    return (10 ** n_digits - 1) // 9 * min(using) 

def lowest_greater_single(using, n):
    return min([x for x in using if x > n], default=-1)

def lowest_greater(using, mini, n_digits):
    # print("lowest_greater")
    highest = mini // (10 ** (n_digits-1))
    rem = mini % (10 ** (n_digits-1))
    if n_digits == 1:
        return mini if mini in using else lowest_greater_single(using, mini)
    if highest in using:
        if rem > largest(using, n_digits-1):
            if lowest_greater_single(using, highest) == -1:
                return -1
            return lowest_greater_single(using, highest) * 10 ** (n_digits-1) + smallest(using, n_digits - 1)
        else:
            return highest * (10 ** (n_digits-1)) + lowest_greater(using, rem, n_digits-1)
    else:
        if lowest_greater_single(using, highest) == -1:
            return -1
        return lowest_greater_single(using, highest) * 10 ** (n_digits-1) + smallest(using, n_digits - 1)

# Codeforce Deltix Round Summer 2021 G
def nbn(mini, using, n_digits, k):
    # print(mini, using, n_digits, k)
    if n_digits == 1:
        if mini in using or k > len(using):
            return mini
        return lowest_greater_single(using, mini)
    if len(using) == k:
        return lowest_greater(using, mini, n_digits)
    else:
        highest = mini // (10 ** (n_digits-1))
        rem = mini % (10 ** (n_digits-1))
        # print(highest, rem)
        if highest in using:
            res = nbn(rem, using, n_digits - 1, k)
            return highest * (10 ** (n_digits-1)) + res
        else:
            res = nbn(rem, using | {highest}, n_digits - 1, k)
            if res != -1:
                return highest * (10 ** (n_digits-1)) + res
            else:
                # print("here",(highest+1) * (10 ** (n_digits-1)))
                return (highest+1) * (10 ** (n_digits-1)) + smallest(using | {highest + 1}, n_digits-1 , len(using | {highest + 1}) < k)

tests = inp()
for _ in range(tests):
    n,k = input_int_gen()
    print(nbn(n,set(),len(str(n)),k))