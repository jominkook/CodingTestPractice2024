#백준 16395 파스칼의 삼각형
# 두번째 풀이
# dp
N,K = map(int,input().split())

dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][0] = 1
    dp[i][i] = 1
    #print(dp[i])

for i in range(2,N):
    for j in range(1,K):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        #print(dp[i])

print(dp[N-1][K-1])





    
