from collections import deque

def solution(m, n, puddles):
    answer = 0
    arr = [[[0,0] for i in range(m)]for _ in range(n)]
    for p in puddles:
        arr[p[0]-1][p[1]-1] = False
    dx,dy = [1,-1,0,0],[0,0,-1,1]
    queue= deque()
    queue.append((0,0))
    arr[0][0][1]=1
    while queue:
        ax,ay = queue.popleft()
        for i in range(4):
            x,y = ax+dx[i],ay+dy[i]
            print(x,y)
            if 0<=x<n and 0<=y<m and arr[x][y]:

                queue.append((x,y))
                arr[x][y][0]=arr[ax][ay][0]+1
                arr[x][y][1]+=arr[ax][ay][1]


    print(arr)
    return answer

solution(4,3,[[2,2]])