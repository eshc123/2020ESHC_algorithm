K, N = map(int,input().split())
LANs = [int(input()) for _ in range(K)]

l,r = 1,max(LANs)

while True:
    if l>r:
        break
    mid = (l+r)//2
    cnt=0
    for lan in LANs:
        cnt+=lan//mid
    if N <= cnt:
        l = mid+1
    else :
        r = mid-1
print(r)