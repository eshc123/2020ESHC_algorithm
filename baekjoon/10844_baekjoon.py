T= int(input())
d=[[0 for _ in range(0,10)] for i in range(T+1)]
for i in range(1,10):
    d[1][i]=1
for i in range(2,T+1):
    for j in range(10):
        if j-1 >= 0:
            d[i][j] += d[i-1][j-1]
        if j+1 <= 9:
            d[i][j] += d[i-1][j+1]
        d[i][j] %= 1000000000
print(sum(d[T])%1000000000)