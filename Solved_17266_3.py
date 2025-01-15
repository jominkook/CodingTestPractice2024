N = int(input())
M = int(input())
light = list(map(int, input().split()))

if M == 1:
    print(max(light[0], N - light[0]))
    
else:
    for i in range(M):
        if i == 0:
            max_distance = light[i]
        elif i == M - 1:
            max_distance = max(max_distance, N - light[i])
            
        else:
            dist = light[i] - light[i - 1]
            
            if dist % 2 == 0:
                dist //= 2
            else:
                dist = dist // 2 + 1
                
            max_distance = max(max_distance, dist)
            
    print(max_distance)
        
