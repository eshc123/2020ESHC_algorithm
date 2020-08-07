N, K = map(int, input().split())
p = [-1 for i in range(200001)]
d = [-1 for i in range(200001)]
r = [0 for i in range(200001)]
queue = []
queue.append(N)
p[N] = 1
d[N] = 0
r[N] = N
while queue:
    point = queue.pop(0)
    # print(point,p[point],d[point])
    if point * 2 >= 0 and point * 2 <= 200000 and p[point * 2] == -1:
        r[point * 2] = point
        p[point * 2] = 1
        d[point * 2] = d[point] + 1
        queue.append(point * 2)
    if point - 1 >= 0 and point - 1 <= 200000 and p[point - 1] == -1:
        r[point - 1] = point
        p[point - 1] = 1
        d[point - 1] = d[point] + 1
        queue.append(point - 1)
    if point + 1 >= 0 and point + 1 <= 200000 and p[point + 1] == -1:
        r[point + 1] = point
        p[point + 1] = 1
        d[point + 1] = d[point] + 1
        queue.append(point + 1)

print(d[K])
t = K
stack = [t]
while True:
    if N == K:
        break
    stack.append(r[t])
    t = r[t]
    if t == N:
        break
for i in stack[::-1]:
    print(i, end=" ")