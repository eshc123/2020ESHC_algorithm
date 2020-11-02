from collections import deque

def solution(priorities, location):
    answer = 0
    q_priorities = deque([i, v] for i, v in enumerate(priorities))
    queue = deque()
    temp_queue = deque()
    for i in range(9,0,-1):
        while q_priorities:
            p = q_priorities.popleft()
            if p[1]==i:
                queue.append(p)
                while temp_queue:
                    q_priorities.append(temp_queue.popleft())
            else:
                temp_queue.append(p)
        q_priorities = temp_queue.copy()
        temp_queue.clear()
    for i,v in enumerate(queue):
        if v[0]==location:
            answer = i+1
    return answer