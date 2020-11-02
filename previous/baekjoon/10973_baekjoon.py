def permutation(n,a):
    idx = -1
    for i in range(n-1,0,-1):
        if arr[i-1]>arr[i]:
            idx = i-1
            break
    if idx == -1:
        print(idx)
    else :
        mx= 0
        for i in range(idx+1,n):
            if mx < arr[i] < arr[idx] :
                mx = arr[i]
                maxdex = i
        arr[idx],arr[maxdex]=arr[maxdex],arr[idx]
        a = arr[:idx+1] + sorted(arr[idx+1:],reverse=True)
        for i in a:
            print(i, end=" ")


N = int(input())

arr = list(map(int,input().split()))

permutation(N,arr)
