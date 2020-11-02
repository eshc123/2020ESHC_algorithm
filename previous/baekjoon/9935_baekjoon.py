string= input()
boom = input()
l = len(boom)
stack = []
for idx in range(len(string)):
    stack.append(string[idx])
    #print(stack)
    if len(stack)>= l and boom==("").join(stack[-l:]):
        for i in range(l):
            stack.pop()

print(("").join(stack) if stack else "FRULA")
