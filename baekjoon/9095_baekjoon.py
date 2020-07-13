T = int(input())
d=[0] * 12
d[1]=1
d[2]=d[1]+1
d[3]=d[1]+d[2]+1
for i in range(4,12):
    d[i]=d[i-1]+d[i-2]+d[i-3]

for _ in range(T):
    n = int(input())
    print(d[n])