while True:
    arr = list(map(int,input().split()))
    if arr[0] == -1 :
        break
    cnt = 0
    for i in arr[:-1]:
        if i*2 in arr[:-1]:
            cnt+=1
    print(cnt)