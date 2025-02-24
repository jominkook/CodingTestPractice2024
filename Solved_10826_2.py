#백준 10826번 피보나치 수 4
# dp로 풀기
# 2번째 풀이
N = int(input())

dp = [0] * 10001

dp[0] = 0
dp[1] = 1
dp[2] = 1


for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[N])