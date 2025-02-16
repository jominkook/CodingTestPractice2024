# 백준 9655번 돌 게임
# dp
# 4번째 풀이
N = int(input())

dp = [0] * 1001

dp[0] = 0
dp[1] = 1

for i in range(2, 1001):
    dp[i] = 1 - dp[i - 1]
    
if dp[N] == 1:
    print("SK")
else:
    print("CY")