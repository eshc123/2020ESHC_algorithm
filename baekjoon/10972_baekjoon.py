def permutation(n,a):
    idx = -1
    for i in range(n-1,0,-1):
        if arr[i-1]<arr[i]:
            idx = i-1
            break
    if idx == -1:
        print(idx)
    else :
        mn= 1000000
        for i in range(idx+1,n):
            if arr[idx] < arr[i] < mn:
                mn = arr[i]
                mindex = i
        arr[idx],arr[mindex]=arr[mindex],arr[idx]
        a = arr[:idx+1] + sorted(arr[idx+1:])
        for i in a:
            print(i, end=" ")


N = int(input())

arr = list(map(int,input().split()))

permutation(N,arr)
