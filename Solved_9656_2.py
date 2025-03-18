N = int(input())

dp = [0] * 1001
dp[1] = 1

for i in range(2, N+1):
    if dp[i-1] == 0:
        dp[i] = 1
    elif i >= 3 and dp[i-3] == 0:
        dp[i] = 1
        
if dp[N] % 2 == 0:
    print('SK')
else:
    print('CY')
    