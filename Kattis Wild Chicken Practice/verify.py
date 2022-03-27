
import sys
input = sys.stdin.readline
def input_string():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])

s = input_string()
stk = []
for c in s:
    if c == "1":
        stk.append(1)
    if c == "d":
        stk.append(stk[-1])
    if c == "+":
        pl = stk.pop() + stk.pop()
        stk = [x-1 for x in stk if x != 1]
        stk.append(pl)
    print(stk)
print(stk)