#유기농배추(BFS)
from collections import deque

T = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(visited,x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and visited[nx][ny] == 1:
                q.append([nx,ny])
                visited[x][y] = 1
                
                                
for i in range(T):
    M ,N ,K = map(int,input().split())
    visited = [[0] * (N) for _ in range(M)]

    for j in range(K):
        x,y = map(int,input().split())
        visited[x][y] = 1

    cnt = 0
    for a in range(M):
        for b in range(N):
            if visited[a][b] == 1:
                bfs(visited,a,b)
                cnt += 1

    print(cnt)
