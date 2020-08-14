N = list(map(int,input()))
s= ''
if 0 in N:
    if sum(N)%3==0:
        N.sort(reverse=True)
        for i in N:
            s+=str(i)
        print(s)
    else:
        print(-1)
else:
    print(-1)
