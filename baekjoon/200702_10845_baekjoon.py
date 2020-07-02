from collections import deque
import sys
T = int(sys.stdin.readline())
queue = deque()
for i in range(T):
    command, *number = sys.stdin.readline().split()
    if command == "push":
        queue.append(number[0])
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else :
            print(-1)
    elif command == "front":
        if queue:
            print(queue[0])
        else :
            print("-1")
    elif command == "back":
        if queue:
            print(queue[-1])
        else :
            print("-1")
    elif command== "size":
        print(len(queue))
    elif command== "empty":
        if queue:
            print(0)
        else :
            print(1)