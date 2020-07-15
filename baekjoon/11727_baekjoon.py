T = int(input())
d = [0] * (T+1)
d[1]=1

if T!=1:
    d[2] = 3
    for i in range(3,T+1):
        d[i]=(d[i-2]*2+d[i-1])%10007
print(d[T])