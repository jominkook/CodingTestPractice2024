#백준 14916번 문제: 거스름돈
#dp문제
#3번째 풀이
N = int(input())

dp = [0] * 100001
dp[0] = -1
dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[4] = 2
dp[5] = 1

for i in range(6, N+1):
    if dp[i-2] == -1 and dp[i-5] == -1:
        dp[i] = -1
    elif dp[i-2] == -1:
        dp[i] = dp[i-5] + 1
    elif dp[i-5] == -1:
        dp[i] = dp[i-2] + 1
    else:
        dp[i] = min(dp[i-2], dp[i-5]) + 1
        
print(dp[N])

        
    
    
        