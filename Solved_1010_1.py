#백준 1010 다리 놓기
#조합공식:nCr = n! / (r! * (n-r)!)
#DP를 이용한 조합공식 사용
#첫번째 풀이


import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 31

dp[0] = 1

#N!을 미리 구해놓는다.
for i in range(1, 31):
    dp[i] = dp[i-1] * i
    
for _ in range(T):
    N, M = map(int, input().split())
    # n! / (r! * (n-r)!)
    print(dp[M] // (dp[N] * dp[M-N]))
    
    

    
    