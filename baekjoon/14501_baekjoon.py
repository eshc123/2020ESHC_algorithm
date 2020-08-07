def resign(prf, idx):
    global maximum
    if idx >= N + 1:
        return
    if idx >= G + 1:
        maximum = max(maximum, prf)
        return

    resign(prf + arr[idx][1], idx + arr[idx][0])
    resign(prf, idx + 1)


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
G = 0
maximum = 0
for i in range(len(arr)): # 일할 수 있는 마지막 날 구하기
    if arr[i][0] + i <= N: # 일하는 당일에서 소요기간을 더해서 퇴사일 보다 적거나 같으면 마지막 날 가능
        G = i
resign(0, 0)
print(maximum)