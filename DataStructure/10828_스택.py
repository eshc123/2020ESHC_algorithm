import sys
T = int(sys.stdin.readline())
stack=[]
for i in range(T):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        stack.append(cmd[1])
    elif cmd[0]=='pop':
        if stack==[]:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif cmd[0]=='size':
        print(len(stack))
    elif cmd[0]=='empty':
        if stack==[]:
            print(1)
        else:
            print(0)
    elif cmd[0]=='top':
        if stack==[]:
            print(-1)
        else:
            print(stack[-1])