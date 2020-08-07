from collections import deque


def dfs(x,stack,fp):
    if x in fp:
        return fp
    #visited[x]=1
    fp
    #stack.append(x)
    if arr[x]:
        for i in arr[x]:
            if i not in stack and i != fp[-1]:
                dfs(i,stack,fp+[i])

#    stack.pop()
    #return a


T = int(input())
arr = [[] for __ in range(T+1)]
visited = [0 for __ in range(T+1)]
for i in range(T):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,T+1):
    if visited[i]==0:
        print(dfs(i, deque(),[]))
