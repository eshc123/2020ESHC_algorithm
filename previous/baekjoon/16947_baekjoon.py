from collections import deque


def dfs(start,now,c,fp):
    if c[now] is True:
        if now == start:
            return fp
    c[now]=True
    for nxt in arr[now]:
        dfs(start,nxt,c,fp+[now])
    return

T = int(input())
arr = [[] for __ in range(T+1)]
check = [False for __ in range(T+1)]
for i in range(T):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,T+1):
    print(dfs(i,i, check,[]))
