#백준 17484 진우의 달 여행
# dfs 풀이
N,M = map(int,input().split())

graph = [[] * M for _ in range(N)]
result = 1000000000

dy = [-1,0,1]

for i in range(N):
    graph[i] = list(map(int,input().split()))
    
def dfs(px,py,pd,cul):
    global result
    if px == N-1:
        result = min(result,cul)
        return
    
    for i in range(3):
        ny = py + dy[i]
        if pd != i and 0 <= ny < M:
            dfs(px+1,ny,i,cul+graph[px+1][ny])
            
for i in range(M):
    dfs(0,i,-1,graph[0][i])
    
print(result)

       
