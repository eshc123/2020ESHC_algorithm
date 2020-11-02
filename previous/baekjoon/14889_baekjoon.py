#비트마스크 이용

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


T = int(input())
arr = [list(map(int,input().split())) for i in range(T)]
m = 10 ** 8
for i in range(1, (1<<T)//2):

    start = []
    link = []
    for j in range(T):
        if i & (1<<j):
            start.append(j)
        else:
            link.append(j)

    if len(start) == len(link):
        t = sub(start, link)
        if m > t:
            m = t
print(m)
