T = int(input())
for i in range(T):
    s = map(list,input().split()) #스택으로 풀기 위해 리스트로 변환
    for word in s:
        while len(word)!=0:
            print(word.pop(),end="") #역순으로 출력하기 위해 pop() 이용
        print(" ",end="")
    print("")
