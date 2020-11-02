import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        if op[0]=="I":
            heapq.heappush(heap,int(op.split()[-1]))
        else:
            if heap:
                if op.split()[-1]=="1":
                    heap = sorted(list(heap))
                    heap.pop()
                    print(heap)
                    heapq.heapify(heap)
                else:
                    print(heap)
                    heapq.heappop(heap)
    if heap:
        return [max(heap),min(heap)]
    else:
        return [0,0]