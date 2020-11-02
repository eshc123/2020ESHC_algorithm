def lotto(n, arr, idx):
    if arr is not None and len(arr) == 6:
        print(' '.join(map(str, arr)))
        return False

    if idx >= n:
        return False

    lotto(n, arr + [S[idx]], idx + 1)
    lotto(n, arr, idx + 1)


while True:
    k, *S = list(map(int, input().split()))
    if k == 0:
        break
    lotto(k, [], 0)
    print()