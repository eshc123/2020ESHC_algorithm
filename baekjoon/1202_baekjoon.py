import sys

N, K = map(int,sys.stdin.readline().split())
jewelry, bags = [list(map(int,sys.stdin.readline().split())) for i in range(N)],[int(sys.stdin.readline()) for i in range(K)]
check_jw = [1 for i in range(N)] # 보석 아직 안 넣었으면 1, 가방에 들어갔으면 0
check_bg = [0 for i in range(K)] # 보석 아직 안 넣었으면 1, 가방에 들어갔으면 0
jewelry.sort(key = lambda x : x[1],reverse=True)
bags.sort()
for idx,bag in enumerate(bags):
    i = 0
    while bag< jewelry[i][0]:
        i+=1
    if check_bg[idx]!=0:
        continue
    if check_jw[i]==1:
        check_bg[idx] = jewelry[i][1]
        check_jw[i] = 0


print(sum(check_bg))
