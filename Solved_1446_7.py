#백준 1446 지름길
# 7번째 풀이

from collections import deque
N,D = map(int,input().split())

distance = [i for i in range(D+1)]
shortcut = []

for i in range(N):
    s,e,l = map(int,input().split())
    shortcut.append([s,e,l])
    

for i in range(D+1):
    if i > 0:
        distance[i] = min(distance[i],distance[i-1]+1)
    for s,e,l in shortcut:
        if i == s and e <= D:
            distance[e] = min(distance[e],distance[s]+l)
        elif i > s and e <= D:
            distance[e] = min(distance[e],distance[s]+l+i-s)
            
print(distance[D])
        
        
        
    
  
    
    
    



        
        
    
    
    
    
