T = int(input())
arr = list(map(int,input().split()))
arr2 = [1 for _ in range(T)]
l,r = 0,0
while l<T:
    if T==1:
        break
    r+=1
    if r<T and arr[l]<arr[r] :
        arr2[r]=max(arr2[l]+1,arr2[r])
    if r==T-1:
        r = l
        l+=1

print(max(arr2))