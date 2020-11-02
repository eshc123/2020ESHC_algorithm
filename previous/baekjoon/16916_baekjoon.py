import sys
import re
S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
p = re.compile(P)
print(0 if not p.search(S) else 1)
# l = len(P)
# for i in range(len(S)-l+1):
#     if S[i:i+l]==P:
#         P = 1
#         break
# print(0 if P!= 1 else 1)