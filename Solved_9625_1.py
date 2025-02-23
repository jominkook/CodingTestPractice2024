K = int(input())

# A,B
dp = [0, 1]
for i in range(2, K+1):
    dp.append(dp[i-1] + dp[i-2])   
print(dp[K-1], dp[K])