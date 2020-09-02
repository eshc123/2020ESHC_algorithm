L = int(input())
s = input()

pi = [0 for i in range(len(s))]

j=0
for i in range(1,len(s)):
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j+=1
        pi[i] = j
print(L-pi[-1])