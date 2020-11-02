from collections import deque


def bfs(q, cnt):
    while q:
        temp = q.popleft()
        nx = temp[0]
        ny = temp[1]
        cnt = temp[2]
        for i in range(4):
            ax = nx + dx[i]
            ay = ny + dy[i]
            if (0 <= ax < N) and (0 <= ay < M):
                if TMT[ax][ay] == 0 and TMT[ax][ay] != -1:
                    TMT[ax][ay] = 1
                    q.append([ax, ay, cnt + 1])
    return cnt


def check(ct):
    for i in range(N):
        for j in range(M):
            if TMT[i][j] == 0:
                return -1
    return ct

dx,dy = [-1,1,0,0],[0,0,-1,1]
M,N = map(int,input().split())
TMT = [list(map(int,input().split())) for _ in range(N)]
c = 0
queue = deque([])

for i in range(N):
    for j in range(M):
        if TMT[i][j] == 1:
            queue.append([i, j, c])
c = bfs(queue, c)

print(check(c))
