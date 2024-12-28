# 1446 지름길문제
# BFS로 풀어보기

# 1. 지름길을 이용하지 않는 경우
# 2. 지름길을 이용하는 경우
# 3. 둘 중 최소값을 선택

import sys
from collections import deque

N, D = map(int, sys.stdin.readline().split())
shortcut = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 0부터 D까지의 거리를 저장할 리스트
distance = [i for i in range(D+1)]


def bfs():
    q = deque()
    q.append(0)

    while q:
        x = q.popleft()

        # 지름길을 이용하지 않는 경우
        if x+1 <= D:
            distance[x+1] = min(distance[x+1], distance[x]+1)
            q.append(x+1)

        # 지름길을 이용하는 경우
        for s, e, d in shortcut:
            if x == s:
                if e <= D:
                    distance[e] = min(distance[e], distance[x]+d)
                    q.append(e)

    return distance[D]


print(bfs())






