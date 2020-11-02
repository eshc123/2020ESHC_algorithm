N = int(input())
arr = list(map(int,input().split()))
cnt=0
for i in range(N):
    for j in range(N-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            cnt+=1
print(cnt)
