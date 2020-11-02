def hanoi(n, f, b, t):
    if n==1:
        arr.append((f, t))
    else:
        hanoi(n-1,f,t,b)
        arr.append((f, t))
        hanoi(n-1,b,f,t)


N = int(input())
arr = []
hanoi(N,1,2,3)
print(len(arr))
for i in arr:
    print(i[0],i[1])