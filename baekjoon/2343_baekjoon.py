def bluelay(m):
    global cnt
    s = 0
    for i in range(N):
        if lessons[i] > m :
            cnt = M +1
            return
        s +=lessons[i]
        if s > m:
            s = lessons[i]
            cnt+=1
    return

N, M = map(int,input().split())
lessons= list(map(int,input().split()))
l,r = 1,sum(lessons)
ans = (l+r)//2
while l<=r:
    mid = (l+r)//2
    cnt = 1
    bluelay(mid)
    if cnt<=M:
        ans = mid
        r = mid-1
    else:
        l = mid + 1
print(ans)
