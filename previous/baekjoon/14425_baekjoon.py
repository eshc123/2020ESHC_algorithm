import sys

N, M = map(int,sys.stdin.readline().split())
S,P= [],[]
cnt = 0
for i in range(N):
    S.append(sys.stdin.readline().rstrip())
for i in range(M):
    P.append(sys.stdin.readline().rstrip())
for p in P:
    if p in S:
        cnt+=1
# for i in range(M):
#     for j in range(N):
#         if P[i] == S[j]:
#             cnt+=1
#             break
print(cnt)