maximum = 0


def byebye(prf, idx):
    global maximum
    if idx >= N + 1:
        return
    if idx >= G + 1:
        maximum = max(maximum, prf)
        return

    byebye(prf + arr[idx][1], idx + arr[idx][0])
    byebye(prf, idx + 1)


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
G = 0
for i in range(len(arr)):
    if arr[i][0] + i <= N:
        G = i
byebye(0, 0)
print(maximum)