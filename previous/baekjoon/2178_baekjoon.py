N, M = map(int,input().split())
a = [list(map(int,input())) for _ in range(N)]
a1 = [[ 0 for _ in range(M)] for _ in range(N)]
check = [[ 0 for _ in range(M)] for _ in range(N)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
queue=list()
queue.append([0,0])
check[0][0]=1
a1[0][0]=1
while queue:
    lst= queue.pop(0)
    for l in range(4):
        nx, ny = lst[0] + dx[l] , lst[1] + dy[l]
        if 0 <= nx < N and 0 <= ny < M:
            if check[nx][ny] != 1 and a[nx][ny] != 0 :
                queue.append([nx,ny])
                a1[nx][ny] = a1[lst[0]][lst[1]]+1
                check[nx][ny] = 1
print(a1[N-1][M-1])