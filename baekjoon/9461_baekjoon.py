T = int(input())
for i in range(T):
    a = int(input())
    P = [0]*101
    P[1]=1
    P[2] = 1
    P[3] = 1
    P[4] = 2
    P[5]=2
    for j in range(6,a+1):
        P[j]=P[j-1]+P[j-5]
    print(P[a])