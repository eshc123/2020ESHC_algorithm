import sys

def dfs(go,cnt):
    global c
    visited[go] = True
    if cnt >= 4:
        c = True
        return

    for i in arr[go]:
        if visited[i] is False :
            dfs(i,cnt+1)
            visited[i] = False
    return


N, M = map(int,sys.stdin.readline().split())
arr = [[] for i in range(N)]
visited = [False for _ in range(N)]
c = False
for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(N):
    dfs(i,0)
    visited[i]=False
    if c:
        break
if c:
    print(1)
else :
    print(0)
