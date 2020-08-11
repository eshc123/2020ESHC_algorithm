def check3by3(x,y,arr1,arr2):
    cnt = 0
    for i in range(x,x+3):
        for j in range(y,y+3):
            if arr1[i][j] != arr2[i][j]:
                cnt+=1
    return cnt


N ,M = map(int,input().split())
before_arr, after_arr = [], []
for i in range(N):
    a=list(map(str,input()))
    before_arr.append(a)
for i in range(N):
    a=list(map(str,input()))
    after_arr.append(a)
cn = 0
while True:
    if before_arr == after_arr:
        break
    m = 0
    cp = [0,0]
    for i in range(N):
        for j in range(M):
            if i+3<=N and j+3<=M:
                c = check3by3(i,j,before_arr,after_arr)
                if m <= c:
                    m=c
                    cp[0]=i
                    cp[1]=j
    for i in range(cp[0],cp[0]+3):
        for j in range(cp[1],cp[1]+3):
            if before_arr[i][j]=="0":
                before_arr[i][j]='1'
            else :
                before_arr[i][j]='0'
    cn+=1
print(cn)