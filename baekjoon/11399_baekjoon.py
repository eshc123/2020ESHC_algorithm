N = int(input())
orders = list(map(int,input().split()))

orders.sort()
times=[]
withdraw =0
for i in orders:
    withdraw += i
    times.append(withdraw)

print(sum(times))