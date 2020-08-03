from collections import deque

def dfs(idx,ar):
    print(idx,end=" ")
    visited[idx]=True
    for i in range(1,N+1):
        if visited[i] is False and i in arr[idx]:
            dfs(i,ar+[i])

    return

def bfs(ar,queue):
    while queue:
        temp = queue.popleft()
        visited1[temp] = True
        for i in sorted(arr[temp]):
            if not visited1[i] and i not in ar:
                ar.append(i)
                queue.append(i)
    for i in ar:
        print(i, end=" ")
    return



N, M, V = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False for i in range(N+1)]
dfs(V,[V])
print()
visited1 = [[] for i in range(N+1)]
bfs([V],deque([V]))
