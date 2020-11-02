# 재귀
def one_two_three(n,s,idx,N):
    global arr
    if n == 0:
        arr.append(s)
        return
    if idx == N:
        return
    one_two_three(n-1,s+[1],idx+1,N)
    one_two_three(n - 2,s+[2],idx+1,N)
    one_two_three(n - 3,s+[3],idx+1,N)


T = int(input())
for i in range(T):
    n = int(input())
    arr = []
    one_two_three(n, [], 0, n)
    print(len(arr))

'''
# 다이내믹 프로그래밍
T = int(input())
d=[0] * 12
d[1]=1
d[2]=d[1]+1
d[3]=d[1]+d[2]+1
for i in range(4,12):
    d[i]=d[i-1]+d[i-2]+d[i-3]

for _ in range(T):
    n = int(input())
    print(d[n])
'''