# 백준 2531_5 회전초밥
# 5번째 풀이과정

n,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]
sushi += sushi[:k-1]

dish = [0]*(d+1)

for i in range(k):
    dish[sushi[i]] += 1
    

cnt = len(set(sushi[:k]))
result = cnt

for i in range(n):
    dish[sushi[i]] -= 1
    if dish[sushi[i]] == 0:
        cnt -= 1
    if dish[sushi[(i+k)%n]] == 0:
        cnt += 1
    dish[sushi[(i+k)%n]] += 1
    result = max(result,cnt + (c not in sushi[i+1:i+k+1]))
    
print(result)