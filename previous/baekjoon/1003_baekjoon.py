T = int(input())
fib = [[1,0],[0,1]]
for i in range(2,41):
    fib.append([fib[i-1][0]+fib[i-2][0],fib[i - 1][1] + fib[i - 2][1]])
for _ in range(T):
    t = int(input())
    print(fib[t][0],fib[t][1])