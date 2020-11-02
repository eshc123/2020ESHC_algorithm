N = int(input())
arr = list(map(int,input().split()))
mn = arr[0]
a = [arr[0]]
for i in arr[1:]:
    if i<arr[-1]:
        pass