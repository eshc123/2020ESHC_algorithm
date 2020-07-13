import sys

def find_prime(n):
    if n==1:
        return False
    else:
        for j in range(2,int(n**0.5)+1):
            if n%j==0:
                return False
        return True

T = int(sys.stdin.readline())
for n in range(T):
    primeList = []
    cnt = 0
    inputValue = int(sys.stdin.readline())
    for i in range(1, inputValue+1):
        if find_prime(i):
            primeList.append(i)
    for j in primeList:
        if inputValue-j < j :
            break
        if inputValue-j in primeList:
            cnt+=1

    print(int(cnt))
