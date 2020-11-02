def solution(triangle):
    answer = 0
    temp=[]
    for row in triangle:
        lst = []
        if len(temp) == 0:
            lst.append(row[0]);
        else:
            for idx, num in enumerate(row):
                if idx == 0:
                    lst.append(temp[-1][idx] + num)
                elif idx == len(row)-1:
                    lst.append(temp[-1][-1] + num)
                else:
                    lst.append(max(temp[-1][idx-1],temp[-1][idx]) + num)
        temp.append(lst)
    return max(temp[-1])