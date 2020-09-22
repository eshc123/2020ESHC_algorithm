def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = sum([i[0]*i[1] for i in zip(A,B)])
    return answer