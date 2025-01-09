N,X = map(int,input().split())
visit = list(map(int,input().split()))

sum = 0
for i in range(X):
    sum += visit[i]
    
max_sum = sum
count = 1

for i in range(X,N):
    sum += visit[i]
    sum -= visit[i-X]
    if sum > max_sum:
        max_sum = sum
        count = 1
    elif sum == max_sum:
        count += 1
        
if max_sum == 0:
    print("SAD")
    
else:
    print(max_sum)
    print(count)