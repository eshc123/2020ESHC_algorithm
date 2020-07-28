# 외판원 순회 2
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
    s = 0
    if arr1[arr[N - 1]][arr[0]] == 0:
        return
    s += arr1[arr[N - 1]][arr[0]]
    for i in range(len(arr) - 1):
        if arr1[arr[i]][arr[i + 1]] == 0:
            break
        s += arr1[arr[i]][arr[i + 1]]
        if i == len(arr) - 2:
            arr2.append(s)
    return


N = int(input())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr = [i for i in range(N)]
arr2 = []
s = 0
if arr1[arr[N - 1]][arr[0]] == 0:
    s=10000000
else :
    s+=arr1[arr[N-1]][arr[0]]
for i in range(len(arr)-1):
    if arr1[arr[i]][arr[i + 1]] == 0:
        s = 10000000
        break
    s += arr1[arr[i]][arr[i+1]]
    if i == len(arr)-2:
        arr2.append(s)
while arr[0]==0:
    permutation(N,arr)
print(min(arr2))
