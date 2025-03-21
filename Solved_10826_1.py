# 백준 10826 피보나치 수 4    
# 첫번째 풀이
# DP 연습

n = int(input())

dp = [0] * (n+1)

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])