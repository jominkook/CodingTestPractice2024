#백준 1012 유기농배추
#5번째 풀이

import sys
sys.setrecursionlimit(10000)

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(T):
    M,N,K = map(int,input().split())
    graph = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    
    
    for j in range(K):
        a,b = map(int,input().split())
        graph[a][b] = 1
        
    def dfs(x,y):
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    graph[nx][ny] = -1
                    dfs(nx,ny)
                    
                    
    count = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] > 0 and not visited[i][j]:
                dfs(i,j)
                count += 1
                
    print(count)
        
                    
               

    
    
    
    
    