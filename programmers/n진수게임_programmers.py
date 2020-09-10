def solution(n, t, m, p):
    answer = ''
    def alpha(n):
        if n==10:
            return "A"
        elif n==11:
            return "B"
        elif n==12:
            return "C"
        elif n==13:
            return "D"
        elif n==14:
            return "E"
        elif n==15:
            return "F"
        else:
            return str(n)
    i=0
    while len(answer)<t*m:
        temp = i
        c = ''
        while temp>n-1:
            c+=alpha(temp%n)
            temp//=n
        c+=alpha(temp)
        answer += c[::-1]
        i+=1
    index =0
    temp = ''
    while t>len(temp):
        if (index+1)%m==p%m:
            temp+=answer[index]
        index+=1
    return temp