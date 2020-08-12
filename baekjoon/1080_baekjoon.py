def change(x,y,arr1,dx,dy):
    for i in range(x,x+dx):
        for j in range(y,y+dy):
            if arr1[i][j] == "0":
                arr1[i][j]="1"
            else :
                arr1[i][j] = "0"
    return


N ,M = map(int,input().split())
before_arr, after_arr = [list(map(str,input())) for i in range(N)], [list(map(str,input())) for i in range(N)]
cn = 0
if N>=3 and M >=3:
    for i in range(N):
        if i >= N-2 :
            break
        for j in range(M):
            if j >= M-2:
                break
            if before_arr[i][j]!=after_arr[i][j]:
                change(i,j,before_arr,3,3)
                cn+=1


if before_arr == after_arr:
    print(cn)
else:
    print(-1)
