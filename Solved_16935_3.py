# 백준 16395    파스칼의 삼각형
# 세번째 풀이
n,k = map(int, input().split())
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for i in range(1,n):
    dp[i][0] = 1
    dp[i][i] = 1
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
print(dp[n-1][k-1])
            