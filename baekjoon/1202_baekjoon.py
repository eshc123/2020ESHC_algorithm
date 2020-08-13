import sys
import heapq
from collections import deque

N, K = map(int,sys.stdin.readline().split())
jewelry, bags = [list(map(int,sys.stdin.readline().split())) for i in range(N)],[int(sys.stdin.readline()) for i in range(K)]
jewelry = deque(sorted(jewelry,key=lambda x: x[0]))
bags = sorted(bags)
heap=[]
cnt=0
for bag in bags:
    capacity=bag
    while jewelry and capacity >= jewelry[0][0]:
        heapq.heappush(heap,-jewelry.popleft()[1])
    if heap:
        cnt-=heapq.heappop(heap)
print(cnt)