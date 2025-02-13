#백준 4963 섬의개수
# 백트래킹(dfs)
# 첫번째 풀이

import sys
sys.setrecursionlimit(10**6)

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    graph = []
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    visited = [[False] * W for _ in range(H)]
    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    dfs(nx, ny)
                    

    for i in range(H):
        graph.append(list(map(int, input().split())))
        
    count = 0

    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1   
    print(count)
    
   


    
    

                
        
                

                
                
        