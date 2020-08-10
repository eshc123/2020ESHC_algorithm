import sys

N = int(sys.stdin.readline())
schedules = []
conference = []
for i in range(N):
    schedules.append(list(map(int,sys.stdin.readline().split())))
schedules.sort(key = lambda x : (x[1],x[0]))
conference.append(schedules[0])
for schedule in schedules[1:]:
    if conference[-1][1] == schedule[0] and conference[-1][1] == schedule[1]:
        conference.append(schedule)
        continue
    if conference[-1][1] <= schedule[0] :
        conference.append(schedule)
print(len(conference))