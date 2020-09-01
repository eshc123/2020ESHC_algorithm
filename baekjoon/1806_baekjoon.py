import sys

N, S = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

l = r = k = s = 0
ans = 100000001
while True:
    if s >= S: # 수열의 총합인 s가 S보다 크면
        ans = min(ans, k) # 현재 가장 낮은 수열의 길이와 현재 구해진 수열의 길이를 비교해서 더 낮은 값으로 갱신
        s -= arr[l] # 수열의 총합에서 가장 왼쪽에 값을 빼고
        l += 1 # 왼쪽 인덱스 값을 늘리면
        k -= 1 # 수열의 길이가 줄어든채 while문이 다시 돈다
    else: ##여기서 먼저 시작, 만약 s가 S보다 작으면 계속해서 수열의 길이를 늘려서 0에서 시작했을때 최대 N-1까지의 길이의 수열이 만들어짐.
        if r == N: # right가 N과 같으면 수열의 범위를 벗어나므로 break
            break
        s += arr[r] #s에 수열의 가장 오른쪽에 있는 값을 누적해서 더한다.
        r += 1 # 오른쪽 인덱스를 1늘린다
        k += 1 # 1늘린만큼 수열의 길이도 증가
print(ans if ans != 1e9 else 0)

