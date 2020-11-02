T=int(input())
stack=[]
result=[]
last_number=1
for i in range(T):
    t=int(input())
    for j in range(last_number,t+1):
        stack.append(j)
        result.append("+")
        last_number=t+1
    if stack[-1]==t:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)
for i in result:
    print(i)