N,X = map(int,input().split())
visit = list(map(int,input().split()))
sumDay = sum(visit[:X])
maxSum = sumDay
maxCount = 1
if sumDay == 0:
    print("SAD")
    exit()

for i in range(X,N):
    sumDay = sumDay - visit[i-X] + visit[i]
    if sumDay > maxSum:
        maxSum = sumDay
        maxCount = 1
    elif sumDay == maxSum:
        maxCount += 1
        
print(maxSum)
print(maxCount)