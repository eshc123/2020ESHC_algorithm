from collections import deque

S = int(input())
queue = deque()
d = [[-1]*(S+1) for _ in range(S+1)]
queue.append((1,0))
d[1][0] = 0


while queue:
    s,c=queue.popleft()
    if d[s][s]==-1:
        d[s][s]=d[s][c]+1
        queue.append((s,s))
    if s+c<=S and d[s+c][c]==-1:
        d[s+c][c]=d[s][c]+1
        queue.append((s+c,c))
    if s-1>=0 and d[s-1][c]==-1:
        d[s-1][c]=d[s][c]+1
        queue.append((s-1,c))

print(min(d[S][1:]))