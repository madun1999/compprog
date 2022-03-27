def genprimes(limit): # derived from 
                      # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}            # http://code.activestate.com/recipes/117119/
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
print(list(genprimes(10000)))