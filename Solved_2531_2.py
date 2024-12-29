#2531

n,d,k,c = map(int,input().split())

sushi = [int(input().strip()) for _ in range(n)]

sushi += sushi[:k-1]

kind = [0] * (d+1)

for i in range(k):
    kind[sushi[i]] += 1
    
cnt = 0
for i in range(1,d+1):
    if kind[i] > 0:
        cnt += 1
        
result = cnt

for i in range(k,n+k):
    
    kind[sushi[i-k]] -= 1
    if kind[sushi[i-k]] == 0:
        cnt -= 1
        
    # 새로운 초밥 추가
    kind[sushi[i % n]] += 1
    if kind[sushi[i % n]] == 1:
        cnt += 1
        
    result = max(result,cnt + (1 if kind[c] == 0 else 0))
    
print(result)