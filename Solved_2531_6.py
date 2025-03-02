N,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:k-1]

cnt = [0] * (d+1)
uniqueSushi = 0

for i in range(k):
    if cnt[sushi[i]] == 0:
        uniqueSushi += 1
    cnt[sushi[i]] += 1
    
result = uniqueSushi

for i in range(N):
    if cnt[sushi[i]] == 1:
        uniqueSushi -= 1
    cnt[sushi[i]] -= 1
    
    if cnt[sushi[(i+k)%N]] == 0:
        uniqueSushi += 1
    cnt[sushi[(i+k)%N]] += 1

    if cnt[c] == 0:
        result = max(result, uniqueSushi+1)
    else:
        result = max(result, uniqueSushi)
print(result)




    
