T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [[0] * 15 for _ in range(15)]
    
    #0층 초기화
    for i in range(15):
        dp[0][i] = i
        
    #나머지 층
    for i in range(1,15):
        for j in range(1,15):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
    print(dp[k][n])
    
  
    
    
    
    