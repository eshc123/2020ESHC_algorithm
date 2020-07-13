T = int(input())
for i in range(T):
    stack=[]
    command=input()
    if command[0]==')':
        print('NO')
        continue
    for j in command:
        if j=='(':
            stack.append(j)
        else :
            if len(stack)==0:
                stack.append(j)
                break
            else:
                stack.pop()
    if len(stack)==0:
        print("YES")
    else:
        print("NO")
