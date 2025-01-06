from collections import deque
N,K = map(int, input().split())
visited = [0]*100001
def bfs(N,K):
    q = deque()
    q.append(N)
    visited[N] = 1
    
    while q:
        x = q.popleft()        
        if x == K:
            return visited[x]-1
        for i in (x-1,x+1,x*2):
            if 0<=i<100001 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[x]+1
                
print(bfs(N,K))
    
    