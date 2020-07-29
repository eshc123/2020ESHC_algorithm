import sys

M = int(sys.stdin.readline())
a = 0
for i in range(M):
    s = list(sys.stdin.readline().split())
    if s[0] == "add":
        a = a | (1 << (int(s[1]) - 1))
    elif s[0] == "check":
        if a & (1 << (int(s[1]) - 1)):
            print(1)
        else:
            print(0)
    elif s[0] == "remove":
        a = a & ~(1 << (int(s[1]) - 1))
    elif s[0] == "toggle":
        a = a ^ (1 << (int(s[1]) - 1))
    elif s[0]== "empty":
        a = 0
    elif s[0] == "all":
        a = 0b11111111111111111111
