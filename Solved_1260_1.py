# 백준 1260 DFS와 BFS
# 2번째 풀이
from collections import deque

N,M,V = map(int,input().split())

graph = [[]*M for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(N+1):
    graph[i].sort()
    


def dfs(V):
    visited[V] = True
    print(V,end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(i)
            
def bfs(V):
    q = deque([V])
    visited[V] = False
    while q:
        V = q.popleft()
        print(V,end=' ')
        for i in graph[V]:
            if visited[i]:
                q.append(i)
                visited[i] = False
                       
dfs(V)
print()
bfs(V)
    

