def permutation(n,a):
    global arr

    idx = -1
    for i in range(n-1,0,-1):
        if arr[i-1]<arr[i]:
            idx = i-1
            break
    if idx == -1:
        return idx
    else :
        mn= 1000000
        for i in range(idx+1,n):
            if arr[idx] < arr[i] < mn:
                mn = arr[i]
                mindex = i
        arr[idx],arr[mindex]=arr[mindex],arr[idx]
        arr = arr[:idx+1] + sorted(arr[idx+1:])
        for i in arr:
            print(i, end=" ")
    print()
    return


N = int(input())

arr = [i for i in range(1,N+1)]
for i in arr:
    print(i, end=" ")
print()
while True:
    if permutation(N,arr)==-1:
        break

