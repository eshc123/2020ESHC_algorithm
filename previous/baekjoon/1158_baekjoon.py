from collections import deque

N, K = map(int,input().split())
queue = deque((i+1) for i in range(N))
result = deque()
while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
print("<",end="")
while result:
    if len(result)==1:
        print(result.pop(),end=">")
        break
    print(result.popleft(),end=", ")