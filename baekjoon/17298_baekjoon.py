N = int(input())
numbers = list(map(int,input().split()))
stack = []
answers = [-1 for i in range(N)]
for idx,number in enumerate(numbers):
    while stack and number>numbers[stack[-1]]:
        l=stack.pop()
        answers[l]=number
    stack.append(idx)
for i in answers:
    print(i,end=" ")
