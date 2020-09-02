N = int(input())

dp = [1 for _ in range(91)]
dp[3] = 2
dp[4]=3
for i in range(5,N+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[N])