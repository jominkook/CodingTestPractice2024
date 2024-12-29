N,K = map(int, input().split())
visited = [0]*100001

def bfs():
    q = []
    q.append(N)
    
    while q:
        x = q.pop(0)
        if x == K:
            return visited[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)
                
                
print(bfs())