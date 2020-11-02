import itertools

def solution(numbers):
    def isPrime(n):
        if n==1 or n==0:
            return False
        for i in range(2,int(n**(0.5))+1):
            if n%i==0:
                return False
        return True
    answer = 0
    s = set()
    for i in range(1,len(numbers)+1):
        for p in itertools.permutations(list(numbers), i):
            s.add(int(''.join(p)))
    for i in list(s):
        if isPrime(i):
            answer +=1
    return answer