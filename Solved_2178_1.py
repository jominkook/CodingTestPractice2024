#백준 2178 미로찾기
#첫번째 풀이
from collections import deque
N, M = map(int, input().split())
graph = []
visited = [[0]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    maze = list(map(int, input()))
    graph.append(maze)
    
def bfs(x, y):
    
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[N-1][M-1]


print(bfs(0,0))
  

    
    

    
