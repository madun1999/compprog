import random
N = 200000
MIN = 100
MAX = 100000000000000
ls = []
for _ in range(N):
    ls.append(str(random.randint(MIN, MAX)))
print(" ".join(ls))