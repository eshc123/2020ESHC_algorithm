import sys

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())

    mv = n
    while n!=1:

        if n%2==0 :
            n=n//2
        else:
            n=n*3+1
        mv=max(n,mv)
    print(mv)