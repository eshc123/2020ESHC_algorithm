S = input()
alphabets = [-1 for _ in range(ord('z')-ord('a')+1)]
for i,v in enumerate(S):
    if alphabets[ord(v)-ord('a')] == -1 :
        alphabets[ord(v) - ord('a')] = i
for i in alphabets:
    print(i,end=' ')