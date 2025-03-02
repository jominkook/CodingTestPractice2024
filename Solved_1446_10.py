N,D = map(int,input().split())
shortucts = []
distances = [i for i in range(D+1)]

for i in range(N):
    start,end,length = map(int,input().split())
    shortucts.append((start,end,length))
    
    
for i in range(D+1):
    if i > 0:
        distances[i] = min(distances[i],distances[i-1]+1)
    for start,end,length in shortucts:
        if end > D:
            continue
        if start == i:
            distances[end] = min(distances[end],distances[start]+length)
         
print(distances[D])
        
        