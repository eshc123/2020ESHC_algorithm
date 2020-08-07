from collections import deque

def dfs(nx,ny,bdx,bdy,cnt):
    global check
    if visited[nx][ny]:
        if cnt >= 4:
            check = True
            return True
        else:
            return False
    visited[nx][ny] = arr[nx][ny]
    for i in range(4):
        if bdx * dx[i] + bdy * dy[i] >= 0:
            x, y = nx + dx[i], ny + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == arr[nx][ny]:
                    dfs(x,y,dx[i],dy[i],cnt+1)


# def bfs(stx,sty):
#     queue= deque()
#     queue.append([stx,sty,arr[stx][sty],0,0,1])
#     while queue:
#         nx,ny,alphabet,bdx,bdy,cnt = queue.popleft()
#         for i in range(4):
#             if bdx*dx[i]+bdy*dy[i]>=0:
#                 x,y = nx+dx[i],ny+dy[i]
#                 if 0<=x<N and 0<=y<M:
#                     if not visited[x][y] and alphabet == arr[x][y]:
#                         visited[x][y] = alphabet
#                         queue.append([x,y,visited[x][y],dx[i],dy[i],cnt+1])
#                         continue
#                     else:
#                         if alphabet == arr[x][y]:
#                             if cnt>=4:
#                                 return True
dx, dy = [-1,1,0,0],[0,0,-1,1]
N, M = map(int,input().split())
arr = [list(map(str,input()) )for i in range(N)]
visited = [["" for _ in range(M)] for __ in range(N)]
check = False
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if dfs(i,j,0,0,1):
                break
        if check:
            break
if check:
    print("Yes")
else:
    print("No")
