#백준 9656 돌 게임 2    

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 0

for i in range(5, 1001):
    if dp[i - 1] == 0 or dp[i - 3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0
        
if dp[n] % 2 == 0:
    print("SK")
else:
    print("CY")