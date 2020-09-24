def solution(n):
    answer = ''
    arr =['4','1','2']
    while n>0:
        t = n%3
        answer += arr[t]
        n//=3
        if t==0:
            n-=1
    return answer[::-1]