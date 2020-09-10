import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for scv in scoville:
        heapq.heappush(heap,scv)
    cnt=0
    a = heapq.heappop(heap)
    while heap:
        if heap:
            b = heapq.heappop(heap)
            cnt+=1
        heapq.heappush(heap,a+ b*2)
        a = heapq.heappop(heap)
        if a >=K:
            return cnt
        else:
            b=0
    return -1