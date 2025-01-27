# 백준 17266 어두운 굴다리
# 4번째 풀이


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
            distance = light[i+1] - light[i]
            
            if distance % 2 == 0:
                distance //= 2
                
            else:
                distance = distance // 2 + 1
                
            max_distance = max(max_distance, distance)
            
    print(max_distance)