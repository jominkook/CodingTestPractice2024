import heapq

def dijkstra(D, shortcuts):
    # 각 위치까지의 최소 거리를 저장할 리스트
    distance = [i for i in range(D + 1)]
    
    # 우선순위 큐를 사용하여 다익스트라 알고리즘 구현
    pq = []
    heapq.heappush(pq, (0, 0))  # (거리, 위치)
    
    while pq:
        current_dist, x = heapq.heappop(pq)
        
        # 현재 위치에서 지름길을 타고 이동할 수 있는 경우
        for start, end, length in shortcuts:
            if start == x and end <= D:
                if distance[end] > current_dist + length:
                    distance[end] = current_dist + length
                    heapq.heappush(pq, (distance[end], end))
        
        # 현재 위치에서 이동할 수 있는 경우
        if x + 1 <= D:
            distance[x + 1] = min(distance[x + 1], current_dist + 1)
            heapq.heappush(pq, (distance[x + 1], x + 1))
    return distance[D]

# 입력 처리
N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(dijkstra(D, shortcuts))