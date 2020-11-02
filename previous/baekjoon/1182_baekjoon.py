#비트마스크 이용
N, S = map(int,input().split())
arr = list(map(int,input().split()))
cnt=0
for i in range(1,(1<<N)):
    s=0
    for j in range(0,N):
        if i & (1<<j):
            s+=arr[j]
    if s==S:
        cnt+=1
print(cnt)

''' 재귀로 푼거
cnt = 0
def booboon(arr, idx):
    global cnt
    if sum(arr) == S and idx >= N and len(arr) > 0:
        cnt += 1
        return
    if idx >= N:
        return

    booboon(arr + [a[idx]], idx + 1)
    booboon(arr, idx + 1)


N, S = map(int, input().split())

a = list(map(int, input().split()))

booboon([], 0)
print(cnt)
'''