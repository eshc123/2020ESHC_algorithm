N, M = map(int,input().split())
c=[[0 for _ in range(300)] for __ in range(300)]

for i in range(1,300):
    for j in range(1,300):
        if c[i][j]==0:
            c[i][j]=min(c[i-1][j],c[i][j-1])+1
print(c[2][2])