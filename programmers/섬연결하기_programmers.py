def solution(n, costs):
    answer = 0
    INF = max(costs, key=lambda x: x[2])[2] + 1
    adj_mat = [[INF for _ in range(n)] for _ in range(n)]
    for cost in costs:
        adj_mat[cost[0]][cost[1]] = cost[2]
        adj_mat[cost[1]][cost[0]] = cost[2]

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
            visited[node] = True  # node 를 방문했다 표시

            for j in range(node_num):
                if adj_mat[node][j] != INF:
                    if not visited[j] and adj_mat[node][j] < distances[j]:
                        distances[j] = adj_mat[node][j]

    prim(0, node_num)

    return sum(distances)