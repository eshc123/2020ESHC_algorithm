N, K = map(int,input().split())
coins = []
cnt=0
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
for coin in coins:
    if coin > K:
        continue
    else :
        cnt += K//coin
        K %= coin
print(cnt)
