T = int(input())
for i in range(T):
    n= int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    d = [[0 for _ in range(n)] for __ in range(2)]
    for j in range(n):
        for k in range(2):
            if j==0:
                d[k][j]= arr[k][j]
            elif j==1:
                if k==0:
                    d[k][j] = arr[k][j]+d[1][j-1]
                else:
                    d[k][j] = arr[k][j]+d[0][j-1]
            else:
                if k == 0:
                    d[k][j] = max(arr[k][j] + d[1][j-1],arr[k][j] +d[1][j-2],arr[k][j] +d[0][j-2])
                else:
                    d[k][j] = max(arr[k][j] + d[0][j-1],arr[k][j] +d[1][j-2],arr[k][j] +d[0][j-2])
    print(max(d[0][n-1],d[1][n-1]))