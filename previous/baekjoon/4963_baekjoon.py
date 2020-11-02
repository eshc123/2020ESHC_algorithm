from collections import deque
import sys
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:
        q = queue.popleft()
        arr[q[0]][q[1]] = 0
        for i in range(8):
            nx, ny = q[0]+dx[i],q[1]+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if arr[nx][ny]==1:
                    arr[nx][ny] = 0
                    queue.append([nx,ny])
            else:
                continue
    return 1


dx,dy = [-1,1,0,0,1,1,-1,-1],[0,0,-1,1,1,-1,1,-1]
while True:
    w,h = map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                cnt+=bfs(i,j)
    print(cnt)