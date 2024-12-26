# 숨바꼭질 1697
N,K = map(int,input().split())
visited = [0]*100001
def bfs():
    q = [N]
    while q:
        x = q.pop(0)
        if x == K:
            print(visited[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0<=nx<100001 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)
                
bfs()
