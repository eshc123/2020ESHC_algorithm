# 일반 python3로 돌리면 시간 초과, pypy3 로 돌리니 맞았음.. 어떻게 시간 단축을 할지 고민해봐야함

import sys

def sub(arr1,arr2):
    s1 , s2 = 0,0
    for i in arr1:
        for j in arr1:
            if i==j:
                continue
            s1+=arr[i][j]
    for i in arr2:
        for j in arr2:
            if i==j:
                continue
            s2+=arr[i][j]
    return abs(s1-s2)


def divide(idx,a):
    global m
    if len(a)!=0 and idx >= T-1:
        t= sub(list(set(s)-set(a)),a) # 시간 초과 원인
        if m > t:
            m = t

        return m
    if idx == T-1:
        return
    divide(idx + 1,a+[s[idx]] )
    divide(idx+1,a)

m = 10 ** 8
T = int(sys.stdin.readline())
s = list(range(T))
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]

divide(0,[])
print(m)