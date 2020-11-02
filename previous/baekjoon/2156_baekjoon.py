n = int(input())
arr = [0 for __ in range(n+1)]
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    g = int(input())
    arr[i], dp[i] = g, g
if n>1:
    dp[2]+=dp[1]
for j in range(3,n+1):
    dp[j]=max(dp[j-1],arr[j]+arr[j-1]+dp[j-3],arr[j]+dp[j-2])
print(max(dp))
