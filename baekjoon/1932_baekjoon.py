T = int(input())
triangle = [[-1 for _ in range(T)] for __ in range(T)]
d = [[0 for _ in range(T)] for __ in range(T)]
dx,dy = [0, 1], [1,1]
for i in range(T):
    triangle[i]=list(map(int,input().split()))+([-1]*(T-i-1))
d[0][0]=triangle[0][0]
for i in range(0,T-1):
    for j in range(i+1):
        if triangle[i][j] != -1:
            d[i+1][j]=max(d[i+1][j],d[i][j]+triangle[i+1][j])
            d[i+1][j + 1] = max(d[i+1][j+1],d[i][j] + triangle[i + 1][j+1])
print(max(d[T-1]))

