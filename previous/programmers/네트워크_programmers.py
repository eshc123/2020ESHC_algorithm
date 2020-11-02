def solution(n, computers):
    def bfs(i):
        queue.append(i)
        while queue:
            idx = queue.pop(0)
            if a[idx] == False:
                a[idx] = True
            for j, k in enumerate(computers[idx]):
                if a[j] is False and k == 1:
                    queue.append(j)

    answer = 0
    queue = []
    a = [False for i in range(n)]
    queue.append(0)
    for i in range(n):
        if a[i] == False:
            bfs(i)
            answer += 1

    return answer