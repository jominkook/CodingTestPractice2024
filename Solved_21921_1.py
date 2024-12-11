#시간초과 ㅠㅠ
import sys
input = sys.stdin.readline

N,X = map(int,input().split())

visit = list(map(int,input().split()))

if sum(visit[:N]) == 0:
    print("SAD")
    sys.exit()

for i in range(N):
    visit[i] = sum(visit[i:i+X])
    
     
max_visit = max(visit)
max_count = visit.count(max_visit)


print(max_visit)
print(max_count)



