T = int(input())
for i in range(T):
    stack = [];
    brackets = input()
    for j in brackets:
        if j == "(" or j == "{" or j == "[":
            stack.append(j)
        if j == ")":
            if stack.pop() != "(":
                stack.append(j)
                break
        if j == "}":
            if stack.pop() != "{":
                stack.append(j)
                break
        if j == "]":
            if stack.pop() != "[":
                stack.append(j)
                break

    if len(stack) == 0 :
        print("YES")
    else :
        print("NO")
