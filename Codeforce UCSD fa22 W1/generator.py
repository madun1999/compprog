import random
N = 16
ls = []
x = 0
for i in range(N):
    x = x ^ i
    ls.append(str(x))
print(" ".join(ls))