N = int(input())
d = [0] * (N+1)
d[1]=1
for j in range(2,N+1):
    i=j
    if j**(0.5)-int(j**(0.5))==0:
        d[j]=1
        continue
    while i>0:
        d[j]+=d[(int(i**(0.5)))**2]
        i=i-(int(i**(0.5)))**2
print(d[N])