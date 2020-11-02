N = int(input())
towers = list(map(int,input().split()))
stack = []
answers = [0 for i in range(N)]
for idx,tower in enumerate(towers):
    while stack:
        if towers[stack[-1]]<tower:
            stack.pop()
        elif towers[stack[-1]]>tower:
            answers[idx] = stack[-1]+1
            break

    stack.append(idx)
for answer in answers:
    print(answer,end=" ")