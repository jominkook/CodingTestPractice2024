#백준 1,2,3 더하기 4
# dp(동적 프로그래밍)
# 세번째 풀이

import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 10001
dp[0] = 1

for i in range(1, 4):
    for j in range(i, 10001):
        if j - i >= 0:
            dp[j] += dp[j - i]
   
for i in range(T):
    N = int(input())    
    print(dp[N])
  
    

        
