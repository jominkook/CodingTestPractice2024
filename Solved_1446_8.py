N,D = map(int,input().split())
distances = [i for i in range(D+1)]
shortcuts = []

for i in range(N):
    shortcuts.append(list(map(int,input().split())))
    
for i in range(D+1):
    if i > 0:
        distances[i] = min(distances[i],distances[i-1]+1)
    for j in range(N):
        if i == shortcuts[j][0]:
            distances[i+shortcuts[j][1]] = min(distances[i+shortcuts[j][1]],distances[i]+shortcuts[j][2])
            
print(distances[D])



    
    



            
            
            



    
    


    



  


    


    


