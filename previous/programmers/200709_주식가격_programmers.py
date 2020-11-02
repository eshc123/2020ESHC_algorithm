from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        time = 0
        price = prices.popleft()
        for index,value in enumerate(prices):
            if price >value:
                time = index+1
                break
            if index == len(prices)-1:
                time = index+1
        answer.append(time)
    return answer