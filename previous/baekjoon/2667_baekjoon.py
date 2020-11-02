def go(index1,index2,cnt):
    if check[index1][index2] == 1 or a[index1][index2]==0:
        return
    check[index1][index2] = 1
    for i in range(4):
        if index1+dx[i]>=0 and index1+dx[i]<T and index2+dy[i]>=0 and index2+dy[i]<T:
            if a[index1+dx[i]][index2+dy[i]] == 1 and check[index1+dx[i]][index2+dy[i]] == 0:
                cnt=go(index1+dx[i],index2+dy[i],cnt+1)
    return cnt
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

T = int(input())
check = [[0 for _ in range(T)] for i in range(T)]
a = [list(map(int,list(input()))) for _ in range(T)]

result=[]
for i in range(T):
    for j in range(T):
        if check[i][j] == 1 or a[i][j] == 0:
            continue
        result.append(go(i,j,1))
result.sort()
print(len(result),*result,sep="\n")