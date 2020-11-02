N = int(input())
arr = [ int(input()) for i in range(N)]
answer = 0
arr.sort(reverse=True)
for i in range(N):
    arr[i] = arr[i] * (i + 1)

print(max(arr))