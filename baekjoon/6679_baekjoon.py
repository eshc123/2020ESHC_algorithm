def ten(n):
    sum_num=0
    while n>0:
        sum_num+=n%10
        n=n//10
    return sum_num

def twelve(n):
    sum_num = 0
    while n > 0:
        sum_num += n % 12
        n = n // 12
    return sum_num

def sixteen(n):
    sum_num = 0
    while n > 0:
        sum_num += n % 16
        n = n // 16
    return sum_num

result=[]
for i in range(1000,10000):
    a=ten(i)
    b=twelve(i)
    c=sixteen(i)
    if a==b and b==c:
        result.append(i)

for i in result:
    print(i)