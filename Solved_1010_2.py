#백준 1010번 다리 놓기
# 조합공식 문제
# nCr = n! / (r! * (n-r)!)
# 2번째 풀이
T = int(input())

dp = [0] * 31

dp[0] = 1

for i in range(1, 31):
    dp[i] = dp[i-1] * i
    
    
for _ in range(T):
    N,M = map(int, input().split())
    
    print(dp[M] // (dp[N] * dp[M-N]))