def assign(m):
    s=0
    for p in provinces:
        if m<=p:
            s+=m
        else:
            s+=p
    return s<=M

N = int(input())
provinces = list(map(int,input().split()))
M = int(input())


provinces.sort()

l,r = 1,max(provinces)
ans = l+ (r-l)//2
while l<=r:
    mid = l+ (r-l)//2
    if assign(mid):
        ans = mid
        l = mid+1
    else:

        r = mid-1
if sum(provinces)<=M:
    print(max(provinces))
else:
    print(ans)
