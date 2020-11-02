T = int(input())
for i in range(T):
    final = int(input())
    d = [1] * (final+1)
    d[0]=0

    for j in range(2,final+1):
        for h in range(j,final+1,j):
            if d[h] == 0 :
                d[h] = 1
            elif d[h] == 1:
                d[h]= 0
    print(sum(d))