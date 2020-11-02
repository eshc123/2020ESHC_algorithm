T = int(input())
for i in range(T):
    s = map(list,input().split())
    for word in s:
        while len(word)!=0:
            print(word.pop(),end="")
        print(" ",end="")
    print("")