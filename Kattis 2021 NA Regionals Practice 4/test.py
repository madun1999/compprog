# def genprimes(limit): # derived from 
#                       # Code by David Eppstein, UC Irvine, 28 Feb 2002
#     D = {}            # http://code.activestate.com/recipes/117119/
#     q = 2

#     while q <= limit:
#         if q not in D:
#             yield q
#             D[q * q] = [q]
#         else:
#             for p in D[q]:
#                 D.setdefault(p + q, []).append(p)
#             del D[q]
#         q += 1
# print(list(genprimes(10000)))


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
aa = [0 for _ in range(5)]
for _ in partitions(2, 2, aa, 0):
    print(aa)
    aa.append(1)
    aa.pop()
    aa[1] += 1
    aa[1] -= 1