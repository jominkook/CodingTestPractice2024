import sys
input = sys.stdin.readline

N,M = map(int,input().split())

dy = [-1,0,1]
graph = [[] for _ in range(N)]
answer = 1000000000
def dfs(px,py,pd,cul):
    if px == N-1:
        answer = min(answer,cul)
        return
    
    for d in range(3):
        ny = py + dy[d]
        
        if (pd != d) and 0 <= ny <M:
            dfs(px+1,ny,d,cul+graph[px+1][ny])
            
for i in range(N):
    graph[i] = list(map(int,input().split()))
    
    
for i in range(M):
    dfs(0,i,-1,graph[0][i])
    
print(answer)
    
    