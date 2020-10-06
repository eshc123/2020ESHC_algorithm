def eratosthenes():
    d = 0
    while len(n) != 0:
        m = n[0]
        cnt = 0
        while cnt < len(n):
            if n[cnt] % m == 0:
                d += 1
                if d == K:
                    return n[cnt]
                n.pop(cnt)
                cnt -= 1
            cnt += 1


N, K = map(int, input().split())
n = list(range(2, N + 1))
print(eratosthenes())