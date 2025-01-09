#백준 2531번 회전 초밥(슬라이딩 윈도우)
#실패
n,d,k,c = map(int,input().split())

sushi = []

for i in range(n):
    sushi.append(int(input()))
    
sushi += sushi[:k-1]

kind = [0] * (d+1)

for i in range(k):
    kind[sushi[i]] += 1
    
cnt = len(set(sushi[:k]))

for i in range(1,d+1):
    if kind[i] > 0:
        cnt += 1
        
result = cnt

for i in range(1,n):
    kind[sushi[i-1]] -= 1
    if kind[sushi[i-1]] == 0:
        cnt -= 1
        
    kind[sushi[(i+k-1)%n]] += 1
    if kind[sushi[(i+k-1)%n]] == 1:
        cnt += 1
        
    if kind[c] == 0:
        result = max(result,cnt+1)
    else:
        result = max(result,cnt)
        
print(result)