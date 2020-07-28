# 차이를 최대로
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
    for i in range(N - 1):
        s += abs(arr[i] - arr[i + 1])
    arr2.append(s)
    return


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr2 = []
s = 0
for i in range(N - 1):
    s += abs(arr[i] - arr[i + 1])
arr2.append(s)
while True:
    if permutation(N,arr)==-1:
        break
print(max(arr2))

