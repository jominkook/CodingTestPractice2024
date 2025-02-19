#백준 2775 부녀회장이 될테야
#dp풀이

T = int(input())

dp = [[0] * 15 for _ in range(15)]
        
        
#0층 초기화
for i in range(15):
    dp[i] = [0] * 15
    dp[0][i] = i
    
#1층부터 14층까지 0층 데이터로 채우기
for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])