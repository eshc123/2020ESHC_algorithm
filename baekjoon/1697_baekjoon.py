N, K = map(int, input().split())
p = [-1 for i in range(200001)]
d = [-1 for i in range(200001)]
queue = []
queue.append(N)
p[N] = 1
d[N] = 0
cnt = 0
while queue:
    point = queue.pop(0)
    # print(point,p[point],d[point])
    if point - 1 >= 0 and point - 1 <= 200000 and p[point - 1] == -1:
        p[point - 1] = 1
        d[point - 1] = d[point] + 1
        queue.append(point - 1)
    if point + 1 >= 0 and point + 1 <= 200000 and p[point + 1] == -1:
        p[point + 1] = 1
        d[point + 1] = d[point] + 1
        queue.append(point + 1)
    if point * 2 >= 0 and point * 2 <= 200000 and p[point * 2] == -1:
        p[point * 2] = 1
        d[point * 2] = d[point] + 1
        queue.append(point * 2)

print(d[K])