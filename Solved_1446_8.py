# 백준 1446 지름길
# shortcuts.append((s,e,l)),shortcuts.append([s,e,l]) 차이
# () => 튜플(불변성) => 메모리를 덜 사용함
# [] => 리스트(변경가능) => 메모리를 더 사용함
N,D = map(int,input().split())
shortcuts = []
distances = [i for i in range(D+1)]

for i in range(N):
    s,e,l = map(int,input().split())
    shortcuts.append((s,e,l))
    print(shortcuts)

for i in range(D+1):
    if i > 0:
        distances[i] = min(distances[i],distances[i-1]+1)
    for s,e,l in shortcuts:
        if e > D:
            continue
        if i == s and e <= D and distances[i] + l < distances[e]:
            distances[e] = distances[i] + l
            
print(distances[D])

    
    
    




    
    



            
            
            



    
    


    



  


    


    


