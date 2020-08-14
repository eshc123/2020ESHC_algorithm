import sys

n = int(input())
if n==0:
    print(0)
    sys.exit()
lectures = [list(map(int,input().split())) for i in range(n)]
lectures.sort(reverse=True,key = lambda x : x[0])
mx = max(lectures,key=lambda x: x[1])
days=[0 for _ in range(mx[1]+1)]
for lecture in lectures:
    if not days[lecture[1]]:
        days[lecture[1]]=lecture[0]
    else:
        for i in range(lecture[1]-1,0,-1):
            if days[i]<lecture[0]:
                days[i]=lecture[0]
                break
print(sum(days))