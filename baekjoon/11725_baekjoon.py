import collections

def bfs(s, parent):
    queue = collections.deque([s])
    visited = [0 for _ in range(n+1)]
    while queue:
        node = queue.popleft()
        visited[node]=1
        for i in tree[node]:
            if visited[i]==0:
                parent[i].append(node)
                queue.append(i)
    return parent


n = int(input())
tree = [[] for _ in range(n+1)]
parents = [[] for _ in range(n+1)]

for _ in range(n-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

for i in list(bfs(1, parents))[2:]:
    print(i[0])

