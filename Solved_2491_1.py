#백준 2491
# 수열

N = int(input())

arr = list(map(int, input().split()))

dp = [1] * N
dp2 = [1] * N


for i in range(1, N):
    if arr[i] >= arr[i-1]:
        dp[i] = dp[i-1] + 1
        
for i in range(1, N):
    if arr[i] <= arr[i-1]:
        dp2[i] = dp2[i-1] + 1
        
print(max(max(dp), max(dp2)))

        
