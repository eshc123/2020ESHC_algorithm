import collections

N, M = map(int,input().split())
B = [[] for _ in range(M+1)]
visited = [ 0 for _ in range(M+1)]
queue = collections.deque()
for i in range(M):
    a,b,c = map(int,input().split())
    B[a].append([b,c])
    B[b].append([a,c])
s,e = map(int,input().split())
queue.append(s)
while queue:
    

#b = [list(map(int,input().split())) for i in range(M)]