from collections import deque

def bfs(start):
    queue = deque()
    queue.append([start[0],start[1]])
    while queue:
        temp=queue.popleft()
        nx=temp[0]
        ny=temp[1]
        if nx == end[0] and ny == end[1]:
            print(arr[nx][ny])
            return
        for i in range(8):
            x = dx[i]+nx
            y = dy[i]+ny
            if 0<=x < a and 0<=y<a:
                if arr[x][y]==0:
                    arr[x][y] = arr[nx][ny]+1
                    queue.append([x,y])



dx,dy=[-2,-2,-1,-1,1,1,2,2],[1,-1,2,-2,2,-2,1,-1]
T = int(input())
for i in range(T):
    a = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    arr = [[0 for _ in range(a)] for __ in range(a)]
    bfs(start)