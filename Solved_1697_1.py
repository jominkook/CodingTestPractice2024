#숨바꼭질 1697
N,K = map(int,input().split())

#방문한 곳을 체크하기 위한 리스트
visited = [0] * 100001

#시작점을 큐에 넣어줌
queue = [N]

#시작점을 방문했다고 표시
visited[N] = 1


while queue:
    #큐에서 하나씩 꺼내옴
    x = queue.pop(0)
    
    #목표지점에 도달하면 멈춤
    if x == K:
        break
    
    #x-1
    if x-1 >= 0 and visited[x-1] == 0:
        queue.append(x-1)
        visited[x-1] = visited[x] + 1
        
    #x+1
    if x+1 <= 100000 and visited[x+1] == 0:
        queue.append(x+1)
        visited[x+1] = visited[x] + 1
        
    #2*x
    if 2*x <= 100000 and visited[2*x] == 0:
        queue.append(2*x)
        visited[2*x] = visited[x] + 1
        
        
        
print(visited[K]-1)

