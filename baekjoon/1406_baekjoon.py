import sys
l1 , T = list(sys.stdin.readline().strip()),int(sys.stdin.readline())
l2 = []
for i in range(T):
    command, *word = sys.stdin.readline().strip()
    if command == 'L' :
        if l1:
            l2.append(l1.pop())
        continue
    elif command == 'D':
        if l2:
            l1.append(l2.pop())
        continue
    elif command == 'P':
        l1.append(word.pop())
    elif command == 'B':
        if l1:
            l1.pop()
        continue
print(''.join(l1+l2[::-1]))