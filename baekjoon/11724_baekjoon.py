from collections import deque
import sys

def bfs(queue):
    global cnt
    while queue:
        q = queue.popleft()
        visited[q]=True
        for el in arr[q]:
            if visited[el] is False:
                visited[el] = True
                queue.append(el)
    cnt +=1

N, M = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt=0
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,N+1):
    if visited[i] is False:
        bfs(deque([i]))
print(cnt)