N = int(input())
r,l,z=[1]*N,[1]*N,[1]*N
for i in range(1,N):
    r[i]=(r[i-1]+z[i-1])%9901
    l[i] = (l[i - 1] + z[i - 1])%9901
    z[i] = (z[i - 1] + r[i - 1]+l[i-1])%9901
print((z[N-1]+r[N-1]+l[N-1])%9901)
