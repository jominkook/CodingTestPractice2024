# 백준 알고리즘 수업 피보나치 수1
# 첫번째 풀이

N = int(input())
dp = [0] * 1001

def fibonacci1(n):
    cnt = 0
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt += 1
        
    return dp[n], cnt

result, cnt = fibonacci1(N)

print(result, cnt)
    



    


    
    