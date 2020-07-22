cnt = 0


def booboon(arr, idx):
    global cnt
    if sum(arr) == S and idx >= N and len(arr) > 0:
        cnt += 1
        return
    if idx >= N:
        return

    booboon(arr + [a[idx]], idx + 1)
    booboon(arr, idx + 1)


N, S = map(int, input().split())

a = list(map(int, input().split()))

booboon([], 0)
print(cnt)