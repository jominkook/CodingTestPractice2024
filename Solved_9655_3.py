# 백준 9655 돌 게임
# 3번째 풀이
# dp를 이용한 풀이 
# 비효율적인 풀이
N = int(input())

dp = [0] * 1001

dp[1] = 1

for i in range(2, N+1):
    if dp[i-1] == 0:
        dp[i] = 1
    else:
        dp[i] = 0
        
if dp[N] == 1:
    print("SK")
    
else:
    print("CY")

