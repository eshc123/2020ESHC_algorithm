def solution(m, n, puddles):
    answer = 0
    arr = [[0 for i in range(m+1)]for _ in range(n+1)]
    arr[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1 :
                continue
            if [j,i] in puddles:
                arr[i][j] = 0
            else:
                arr[i][j] += (arr[i-1][j] + arr[i][j-1]) % 1000000007
    return arr[-1][-1]