# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# INF = max(costs,key = lambda x : x[2])[2]+1
#     adj_mat = [[INF for _ in range(n) ]for _ in range(n)]
#     for cost in costs:
#         adj_mat[cost[0]][cost[1]]=cost[2]
#         adj_mat[cost[1]][cost[0]]=cost[2]

INF = 999
adj_mat = [[0, 29, INF, INF, INF, 10, INF],
           [29, 0, 16, INF, INF, INF, 15],
           [INF, 16, 0, 12, INF, INF, INF],
           [INF, INF, 12, 0, 22, INF, 18],
           [INF, INF, INF, 22, 0, 27, 25],
           [10, INF, INF, INF, 27, 0, INF],
           [INF, 15, INF, 18, 25, INF, 0]]

node_num = len(adj_mat)
visited = [False] * node_num
distances = [INF] * node_num


def get_min_node(node_num):
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        if not visited[i] and distances[i] < distances[v]:
            v = i

    return v


def prim(start, node_num):
    # distances 배열과 visted 배열 초기화
    for i in range(node_num):
        visited[i] = False
        distances[i] = INF

    # 시작노드의 distance 값을 0으로 초기화
    distances[start] = 0
    for i in range(node_num):
        node = get_min_node(node_num)
        visited[node] = True    # node 를 방문했다 표시

        for j in range(node_num):
            if adj_mat[node][j] != INF:
                if not visited[j] and adj_mat[node][j] < distances[j]:
                    distances[j] = adj_mat[node][j]


print(prim(0, node_num))
print("distances: ", distances)
print("minimum cost: ", sum(distances))