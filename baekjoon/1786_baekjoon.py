import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
result = list()
count = 0
pi = [0 for i in range(len(P))]

j=0
for i in range(1,len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j - 1]
    if P[i] == P[j]:
        j+=1
        pi[i] = j

j = 0

patternLength = len(P)
textLength = len(T)
for i in range(0, textLength):
    while j > 0 and T[i] != P[j] :
        j = pi[j - 1]
    if T[i] == P[j] :
        if j == patternLength - 1:
            ##같은 패턴을 찾았음
            result.append(i - patternLength + 2)
            count+=1
            j = pi[j]
        else:
            j+=1

print(count)
for c in result:
    print(c)
