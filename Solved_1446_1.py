#지름길
#실패
N,D = map(int,input().split())

#지름길의 시작점과 끝점을 저장할 리스트
shortcuts = []

for _ in range(N):
    s,e,l = map(int,input().split())
    #지름길의 시작점이 도착점보다 작은 경우에만 추가
    if e-s > l:
        shortcuts.append((s,e,l))
        
#지름길의 시작점을 기준으로 오름차순 정렬
shortcuts.sort()

#dp[i] : i까지 오는데 걸리는 시간
dp = [i for i in range(D+1)]

for i in range(D+1):
    #i까지 오는데 걸리는 시간
    dp[i] = min(dp[i],dp[i-1]+1)
    for s,e,l in shortcuts:
        #지름길의 시작점이 i보다 작은 경우에만
        if s == i:
            dp[e] = min(dp[e],dp[s]+l)
            
print(dp[D])
        
        
        

