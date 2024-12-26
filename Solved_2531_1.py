#2531 회전초밥

N,D,K,C = map(int,input().split())
sushi = []
for i in range(N):
    sushi.append(int(input()))
    
sushi += sushi[:K-1]

answer = 0

for i in range(N):
    temp = sushi[i:i+K]
    temp.append(C)
    answer = max(answer,len(set(temp)))
    
print(answer)
    