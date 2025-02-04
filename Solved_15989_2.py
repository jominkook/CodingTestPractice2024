# 백준 15989 1,2,3 더하기 4
# 2번째 풀이

T = int(input())

dp = [0] * 10001

dp[0] = 1


for i in range(1,4):
    for j in range(i,10001):
        dp[j] += dp[j-i]
        
    
for _ in range(T):
    n = int(input())
    print(dp[n])

