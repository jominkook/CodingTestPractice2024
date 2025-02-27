import sys
sys.setrecursionlimit(10000)
com = int(input())
conections = int(input())
graph  = [[] for _ in range(com+1)]
visited = [False] * (com+1)
cnt = 0
for i in range(conections):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(graph,start,visited):
    global cnt
    visited[start] = True
    cnt += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)
            
            
dfs(graph,1,visited)
print(dfs(graph,1,visited))
print(cnt-1)