N, K = map(int,input().split())
temp = N
n = 0
while True:
    if temp==0:
        temp = N
        break
    n+=1
    temp//=10
idx = 1
cnt=0
while True:
    if idx==n:
        print(cnt)
        t=10**(idx-1)
        # for i in range(cnt,K,idx):
        #     t+=i
        #     cnt+=idx
        #cnt+=(N-(10**(idx-1)-1))*idx
        break
    cnt += ((10 ** idx) - (10 ** (idx - 1)))*idx
    idx+=1
print(t)

