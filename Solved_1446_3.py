#1446 지름길

from collections import deque
N,D = map(int,input().split())

#지름길의 시작점과 끝점을 저장할 리스트
shortcuts = []

#지름길의 시작점과 끝점을 입력받아 shortcuts에 저장
for i in range(N):
    start,end,length = map(int,input().split())
    shortcuts.append([start,end,length])
    

def bfs(D):
    #각 위치까지의 최소거리를 저장할 리스트
    distance = [i for i in range(D+1)]
    
    #거리를 계산할 큐
    q = deque()
    q.append(0)
    
    while q:
        x = q.popleft()
        
        #현재 위치에서 지름길을 타고 이동할 수 있는 경우
        for start,end,length in shortcuts:
            if start == x and end <= D:
                if distance[end] > distance[start] + length:
                    distance[end] = distance[start] + length
                    q.append(end)
                    
        #현재 위치에서 이동할 수 있는 경우
        if x+1 <= D:
            if distance[x+1] > distance[x] + 1:
                distance[x+1] = distance[x] + 1
                q.append(x+1)
                
    return distance[D]


print(bfs(D))
    