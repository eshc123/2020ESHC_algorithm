T = int(input())
stairs = [0 for i in range(301)]
for t in range(1,T+1):
    stairs[t]=(int(input()))
dp = [0 for _ in range(301)]
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]
dp[3] = max(stairs[2]+stairs[3],dp[1]+stairs[3])
for i in range(4,T+1):
    dp[i] = max(stairs[i]+dp[i-2],dp[i-3]+stairs[i-1]+stairs[i])
print(dp[T])