S = input()
alphabets = [0 for _ in range(ord('z')-ord('a')+1)]
for i in S:
    alphabets[ord(i)-ord('a')]+=1
for i in alphabets:
    print(i,end=' ')