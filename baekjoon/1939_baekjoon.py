import collections
import sys

def bfs(w):
    visited = [0 for _ in range(N + 1)]
    queue = collections.deque()
    queue.append(s)
    while queue:
        q = queue.popleft()
        visited[q]=1
        for el in B[q]:
            if visited[el[0]]==0 and el[1]>=w:
                visited[el[0]] = 1
                queue.append(el[0])
    if visited[e]==1:
        return True
    else:
        return False


N, M = map(int,sys.stdin.readline().split())
B = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    B[a].append([b,c])
    B[b].append([a,c])
s,e = map(int,sys.stdin.readline().split())
l,r = 1,1000000000
ans = l
while l<=r:
    mid = (l+r)//2
    if bfs(mid):
        ans = mid
        l=mid+1
    else:
        r=mid-1
print(ans)