#N번째 큰 수 2075
#heapq를 이용하여 풀이
import heapq

N = int(input())

heap = []

for i in range(N):
    for j in list(map(int, input().split())):
        heapq.heappush(heap, j)
        if len(heap) > N:
            heapq.heappop(heap)
            
print(heap[0])

