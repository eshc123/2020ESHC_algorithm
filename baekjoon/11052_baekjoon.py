N = int(input())

p = [0]+list(map(int,input().split()))
d = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        d[i]=max(d[i],p[j]+d[i-j])

print(d[N])