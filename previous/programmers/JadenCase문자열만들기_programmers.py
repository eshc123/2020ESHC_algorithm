def solution(s):
    s = s.lower()
    temp=s.split(" ")
    answer = []
    for i in temp:
        answer.append(i.capitalize())
    return (" ").join(answer)