N, M = map(int,input().split())
c=[[0 for _ in range(N+1)] for __ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        if c[i][j]!=0:
            continue

        if i==1 and j==1:
            c[i][j] = 0
            continue
        elif i==1:
            c[i][j]=j-1
            continue
        elif j==1:
            c[i][j]=i-1
            continue

        c[i][j]=i*j-1

print(c[M][N])