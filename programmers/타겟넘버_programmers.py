def solution(numbers, target):
    answer=0
    temp=[]
    def go(s,idx):
        if idx>=len(numbers):
            if s==target:
                return temp.append(1)
            return
        go(s+numbers[idx],idx+1)
        go(s-numbers[idx],idx+1)
    go(0,0)
    answer = sum(temp)
    return answer