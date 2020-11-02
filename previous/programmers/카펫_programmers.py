import math

def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(math.ceil(float(total**0.5)),total):
        if total%i==0:
            if i*2+(total//i-2)*2==brown:
                answer = [i,total//i]
                break
    return answer