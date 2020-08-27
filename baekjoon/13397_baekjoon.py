def score(m):
    mx = arr[0]
    mn = arr[0]
    cnt=1
    for i in range(1,N):
        mx = max(mx,arr[i])
        mn = min(mn,arr[i])
        if mx - mn > m:
            cnt+=1
            mx = arr[i]
            mn = arr[i]
    return cnt<=M
N, M = map(int,input().split())
arr = list(map(int,input().split()))
l,r = 0, max(arr)
ans = (l+r)//2
while l<=r:
    mid = (l+r)//2
    if score(mid):
        ans = mid
        r = mid -1
    else:
        l = mid + 1
print(ans)