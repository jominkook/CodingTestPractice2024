

n,d,k,c = map(int,input().split())

sushi = []

for i in range(n):
    sushi.append(int(input()))
    
sushi += sushi[:k-1]
kind = [0] * (d+1)

for i in range(k):
    kind[sushi[i]] += 1
cnt = len(set(sushi[:k]))

result = cnt

for i in range(n):
    kind[sushi[i]] -= 1
    if kind[sushi[i]] == 0:
        cnt -= 1
    kind[sushi[(i+k)%n]] += 1
    if kind[sushi[(i+k)%n]] == 1:
        cnt += 1
    result = max(result,cnt + (c not in sushi[i+1:i+k]))
    
print(result)






