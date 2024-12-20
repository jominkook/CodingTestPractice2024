#올림픽문제

N,K = map(int,input().split())

medal = []

for i in range(N):
    medal.append(list(map(int,input().split())))
    
medal.sort(key = lambda x : (-x[1],-x[2],-x[3]))

for i in range(N):
    if medal[i][0] == K:
        idx = i
        break

for i in range(N):
    if medal[i][1:] == medal[idx][1:]:
        print(i+1)
        break
    
    




    
        