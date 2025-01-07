N,D = map(int,input().split())

shortcut = []
distance = [i for i in range(D+1)]

def bfs(D,shortcut):
    for i in range(D+1):
        if i>0:
            distance[i] = min(distance[i],distance[i-1]+1)
        for j in range(N):
            if i == shortcut[j][1]:
                distance[i] = min(distance[i],distance[shortcut[j][0]]+shortcut[j][2])
    return distance[D]


for i in range(N):
    start, end, length = map(int,input().split())
    shortcut.append([start,end,length])
    
print(bfs(D,shortcut))





            
    
    