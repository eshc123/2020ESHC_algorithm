S = int(input())

l,r = 1,S
ans = l+(r-l)//2
while l<=r:
    mid = l+(r-l)//2
    if mid*(mid+1)//2<=S:
        if S < (mid + 1) * (mid + 2) // 2:
            break
        l=mid+1
    else:
        r=mid-1
print(mid)

