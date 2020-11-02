def divide(idx,n):
    global r, c
    if idx==0:
        print(n)
        return

    d = 2 ** (idx - 1)
    if r<d and c>=d:
        n+= d ** 2
        c-= d
    elif r>=d and c<d:
        n+= (d ** 2) * 2
        r-= d
    elif r>=d and c>=d:
        n+= (d ** 2) * 3
        r-= d
        c-=d
    divide(idx-1,n)



N, r, c = map(int,input().split())
divide(N,0)