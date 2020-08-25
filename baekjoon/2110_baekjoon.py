def binary(index, ci,cnt,d):
    global l,r,mid,m
    if index>=len(dist) or ci>len(dist):
        if cnt<C:
            r = mid-1
            return
        else:
            m=mid
            l = mid + 1
            return
    s = sum(dist[index:ci])
    if s >= d:
        binary(ci,ci+1,cnt+1,d)
    else:
        binary(index,ci+1,cnt,d)

N, C = map(int,input().split())
router = [ int(input()) for i in range(N)]
router.sort()
m=0
dist = [router[i+1]-router[i] for i in range(N-1) ]
l, r = min(router),max(router)
while l<=r:
    mid = (r+l)//2
    binary(0,1,1,mid)

print(m)