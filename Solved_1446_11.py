N,D = map(int,input().split())
shortcut = []
distance = [i for i in range(D+1)]


for i in range(N):
    start,end,length = map(int,input().split())
    shortcut.append([start,end,length])


for i in range(D+1):
    if i > 0:
        distance[i] = min(distance[i],distance[i-1]+1)

    for start,end,length in shortcut:
        if end > D:
            continue
        if start == i:
            distance[end] = min(distance[end],distance[start]+length)
            
print(distance[D])

    


        


        
            
            