# import random
# N = 16
# ls = []
# x = 0
# for i in range(N):
#     x = x ^ i
#     ls.append(str(x))
# print(" ".join(ls))

# from itertools import combinations
# from operator import mul
# from functools import reduce
# primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
# ret = []
# for i in range(1,len(primes)+1):
#     l = i % 2
#     prime = primes[:i]
#     sum = 0
#     for i in range(len(prime)):
#         for k in combinations(prime, i):
#             if i % 2 == l:
#                 sum -= reduce(mul, k, 1)
#             else:
#                 sum += reduce(mul, k, 1)
#     ret.append(sum)
# print(ret)

FIRST = 10000
stk = [FIRST]

print("[")
for n in range(1,23):
    print(str(n) + ": " + str(2**n - n))
print("]")
