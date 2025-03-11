N,X = map(int,input().split())

visit = list(map(int,input().split()))

sum = 0
for i in range(X):
    sum += visit[i]
    
max = sum
count = 0

if sum == 0:
    print("SAD")
    exit()
else:
    count += 1
    for i in range(X,N):
        sum = sum - visit[i-X] + visit[i]
        if sum > max:
            max = sum
            count = 1
        elif sum == max:
            count += 1
            
print(max)
print(count)