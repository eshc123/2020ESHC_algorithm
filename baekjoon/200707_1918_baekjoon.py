S = input()
operators = ["+","-","*","/"];
brackets = ["(",")"];
stack1 = list()
stack2 = list()
for i in S :
    if (not i in operators) and (not i in brackets):
        stack1.append(i)
    elif i in brackets:
        if i == brackets[0]: # i== "("일 때
            stack2 = stack1[:]

print(stack1)