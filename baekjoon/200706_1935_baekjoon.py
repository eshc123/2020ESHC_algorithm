N = int(input())
expr = input()
dic = dict()
stack = list()
operations = ["+","-","*","/"]
for i in range(N):
    dic[chr(ord('A')+i)] = int(input())
for i in expr:
    if i in operations:
        temp = str(stack.pop())
        stack.append(eval(str(stack.pop())+i+temp))
    else :
        stack.append(dic.get(i))
print("%0.2f"%stack.pop())
