#백준 2512 예산문제
# 4번째 풀이과정
# dp를 이용한 풀이
N = int(input())

budgets = list(map(int, input().split()))
dp = [0] * 10001
M = int(input())

start = 0
end = max(budgets)

while start <= end:
    mid = (start + end) // 2
    for i in range(N):
        dp[i] = min(budgets[i], mid)
    if sum(dp) > M:
        end = mid - 1    
    else:
        start = mid + 1
print(end)


