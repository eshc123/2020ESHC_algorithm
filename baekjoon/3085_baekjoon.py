def go(x, y, l):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            return l



N = int(input())
arr = [list(input()) for i in range(N)]
result = []
for i in range(N):
    for j in range(N):
        result.append(go(i,j,1))
print(result)