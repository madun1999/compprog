import sys
input = sys.stdin.buffer.readline

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


# Google Kick Start 2021 H Problem B
tests = inp()
for test in range(tests):
    n = inp()
    s = input_string()
    count = 0
    last = {b"R": False, b"Y": False, b"B": False}
    bases = {
        ord("U"): [],
        ord("R"): [b"R"],
        ord("Y"): [b"Y"],
        ord("B"): [b"B"],
        ord("O"): [b"R", b"Y"],
        ord("G"): [b"Y", b"B"],
        ord("P"): [b"B", b"R"],
        ord("A"): [b"R", b"Y", b"B"],
    }

    for c in s:
        bs = bases[c]
        for color in last.keys():
            if color in bs:
                if last[color]:
                    pass
                else:
                    count += 1
                    last[color] = True
            else:
                if last[color]:
                    last[color] = False
                else:
                    pass
    print(f"Case #{test+1}:", count)