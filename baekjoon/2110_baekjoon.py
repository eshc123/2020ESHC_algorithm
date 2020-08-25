import sys

N, C = map(int,sys.stdin.readline().split())
router = [ int(sys.stdin.readline()) for i in range(N)]
router.sort()
l, r = 1,max(router)
while l<=r:
    mid = (r+l)//2
    cnt = 1
    cp = router[0]
    for i in range(1,N):
        if mid+cp<=router[i]:
            cnt+=1
            cp=router[i]

    if cnt < C :

        r = mid-1
    else:
        a = mid
        l = mid+1

print(a)